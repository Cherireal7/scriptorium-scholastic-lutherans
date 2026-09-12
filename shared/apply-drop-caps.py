"""Apply Reedsy-style drop caps to the first body paragraph of each Heading 1.

Post-processor for a built DOCX. Splits the first letter of the first substantive
body paragraph after every Heading 1 into a `framePr dropCap` frame, so the letter
drops down N lines with text wrapping around it. Idempotent — running twice is a
no-op after the first pass (guards against already-frame paragraphs).

Usage:
  python apply-drop-caps.py <docx-path> [options]

Options:
  --skip N        Skip N body paragraphs after each Heading 1 before applying
                  drop cap (default 0). Useful for Q&A/scholastic texts where
                  the first body paragraph is a question echo and you want the
                  drop cap on the answer instead (--skip 1).
  --size PT       Drop cap letter font size in points (default 40).
  --lines N       Number of body lines the drop cap spans (default 3).
  --skip-headings STYLES   Comma-separated list of Heading 1 texts to skip
                           (e.g. "Table of Contents,Translator's Note").

Run with system Python — does not require LibreOffice.
"""

import argparse
import os
import re
import shutil
import sys
import zipfile

W_NS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
W = '{' + W_NS + '}'


def _text_of(p_xml: str) -> str:
    """Return the concatenated visible text of a <w:p> XML string."""
    return ''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', p_xml))


def _paragraph_style(p_xml: str) -> str:
    m = re.search(r'<w:pStyle w:val="([^"]+)"', p_xml)
    return m.group(1) if m else ''


def _has_drop_cap(p_xml: str) -> bool:
    return 'w:dropCap' in p_xml


def _make_drop_cap_paragraph(letter: str, size_pt: int, lines: int) -> str:
    """Build the frame-only paragraph that holds the drop-cap letter."""
    half_pts = size_pt * 2
    return (
        '<w:p><w:pPr>'
        f'<w:framePr w:dropCap="drop" w:lines="{lines}" w:wrap="around" '
        'w:vAnchor="text" w:hAnchor="text" w:xAlign="left" w:yAlign="text"/>'
        '<w:spacing w:line="240" w:lineRule="auto"/>'
        '</w:pPr>'
        f'<w:r><w:rPr><w:position w:val="-4"/><w:sz w:val="{half_pts}"/>'
        f'<w:szCs w:val="{half_pts}"/></w:rPr>'
        f'<w:t xml:space="preserve">{letter}</w:t></w:r></w:p>'
    )


def _split_first_letter(p_xml: str):
    """Remove the first alphabetic letter from a paragraph's first <w:t>.

    Returns (letter, new_p_xml) or (None, p_xml) if no letter found.
    Handles bold/italic runs correctly by only touching the first text.
    """
    m = re.search(r'(<w:t[^>]*>)([^<]*)(</w:t>)', p_xml)
    if not m:
        return None, p_xml
    prefix, text, suffix = m.groups()
    lm = re.search(r'([A-Za-z])', text)
    if not lm:
        return None, p_xml
    letter = lm.group(1)
    new_text = text[:lm.start()] + text[lm.end():]
    # Preserve xml:space if new_text starts with space
    if 'xml:space' not in prefix and (new_text.startswith(' ') or new_text.endswith(' ')):
        prefix = prefix.replace('<w:t', '<w:t xml:space="preserve"', 1)
    new_p_xml = p_xml.replace(m.group(0), prefix + new_text + suffix, 1)
    return letter, new_p_xml


def _iter_paragraphs(document_xml: str):
    """Yield (start_index, end_index, xml_string) for each <w:p> in document.xml."""
    for m in re.finditer(r'<w:p(?:\s[^>]*)?(?:/>|>.*?</w:p>)', document_xml, re.DOTALL):
        yield m.start(), m.end(), m.group(0)


def apply_drop_caps(docx_path: str, *, skip_body: int = 0,
                    size_pt: int = 40, lines: int = 3,
                    skip_headings=None) -> int:
    """Modify a DOCX in place, adding drop caps after each Heading 1.

    Returns the number of drop caps added.
    """
    skip_headings = set(skip_headings or [])

    z = zipfile.ZipFile(docx_path, 'r')
    files = {n: z.read(n) for n in z.namelist()}
    z.close()

    doc = files['word/document.xml'].decode('utf-8')

    # Walk paragraphs, tracking state: after each Heading 1, count body paragraphs
    added = 0
    paras = list(_iter_paragraphs(doc))
    # Build a list of (start, end, xml, is_h1, is_body_candidate, first_letter)
    # then splice modifications from the end (so offsets don't shift).
    modifications = []  # list of (start, end, replacement_xml)

    # Group by "run": each Heading 1 starts a group; skip N body paragraphs;
    # drop-cap the next body paragraph.
    state = 'seeking-h1'
    body_seen = 0
    for start, end, p_xml in paras:
        style = _paragraph_style(p_xml)
        text = _text_of(p_xml).strip()

        is_h1 = style == 'Heading1'
        is_heading = style.startswith('Heading') or style in ('Title', 'Subtitle')
        is_empty = not text
        # skip fleuron dividers and pure-italic Latin subtitles
        is_fleuron = text in ('— ❦ —', '❦', '— ❧ —')
        is_all_italic = bool(re.match(r'^<w:p[^>]*>(?:\s*<w:r[^>]*>(?:\s*<w:rPr[^>]*<w:i/>[^<]*</w:rPr>)?\s*<w:t[^>]*>[^<]*</w:t>\s*</w:r>)+\s*</w:p>$', p_xml))

        if is_h1:
            if text in skip_headings:
                state = 'seeking-h1'
                continue
            state = 'in-chapter'
            body_seen = 0
            continue

        if state != 'in-chapter':
            continue

        if is_heading or is_empty or is_fleuron:
            continue

        # This is a body-candidate paragraph.
        if body_seen < skip_body:
            body_seen += 1
            continue

        # Apply drop cap to this paragraph.
        if _has_drop_cap(p_xml):
            state = 'seeking-h1'
            continue

        letter, new_body_p = _split_first_letter(p_xml)
        if letter is None:
            state = 'seeking-h1'
            continue

        drop_p = _make_drop_cap_paragraph(letter, size_pt, lines)
        modifications.append((start, end, drop_p + new_body_p))
        added += 1
        state = 'seeking-h1'  # move on to next H1

    # Apply modifications from the end to preserve offsets.
    for start, end, repl in reversed(modifications):
        doc = doc[:start] + repl + doc[end:]

    files['word/document.xml'] = doc.encode('utf-8')

    tmp = docx_path + '.dropcap-tmp'
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zw:
        for name, data in files.items():
            zw.writestr(name, data)
    shutil.move(tmp, docx_path)
    return added


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('docx', help='Path to the DOCX to modify in place.')
    ap.add_argument('--skip', type=int, default=0, dest='skip_body',
                    help='Skip N body paragraphs after each H1 before drop-cap.')
    ap.add_argument('--size', type=int, default=40, dest='size_pt',
                    help='Drop-cap letter size in points (default 40).')
    ap.add_argument('--lines', type=int, default=3,
                    help='Body lines the drop cap spans (default 3).')
    ap.add_argument('--skip-headings', default='',
                    help='Comma-separated H1 texts to skip.')
    args = ap.parse_args(argv)

    if not os.path.isfile(args.docx):
        print(f'ERROR: not a file: {args.docx}', file=sys.stderr)
        sys.exit(2)

    skip_headings = [s.strip() for s in args.skip_headings.split(',') if s.strip()]
    added = apply_drop_caps(
        args.docx,
        skip_body=args.skip_body,
        size_pt=args.size_pt,
        lines=args.lines,
        skip_headings=skip_headings,
    )
    print(f'Added {added} drop caps to {args.docx}')


if __name__ == '__main__':
    main()
