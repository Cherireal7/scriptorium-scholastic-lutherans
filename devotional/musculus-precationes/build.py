#!/usr/bin/env python3
"""Build the Musculus Precationes working edition: translation/*.md -> HTML -> PDF.

Usage:  python3 build.py [1573|1561]   (writes review/build-<edition>/book.html and the PDF in review/)
Needs:  Google Chrome (headless print), poppler's pdftotext (for the contents page numbers).
"""
import html, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REVIEW = HERE / "review"
EDITION = sys.argv[1] if len(sys.argv) > 1 else "1573"      # "1573" (enlarged) or "1561" (strict)
SRC = REVIEW / f"translation-{EDITION}"
OUT = REVIEW / f"build-{EDITION}"
FRONT = REVIEW / f"front-{EDITION}.html"
NOTE = REVIEW / f"translators-note-{EDITION}.md"
PDF = REVIEW / f"Andreas-Musculus-Precationes-{EDITION}-English-Scholastic-Lutherans.pdf"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

FLEURON = '<div class="fleuron">— ❦ —</div>'


def inline(s: str) -> str:
    s = html.escape(s, quote=False)
    s = re.sub(r"\{p\.(\d+)\}", r'<span class="pg">[\1]</span>', s)
    s = re.sub(r"\{img\.(\d+)\}", "", s)
    s = re.sub(r"\{f\.(\w+)\}", r'<span class="pg">[\1]</span>', s)
    s = re.sub(r"\[margin:\s*(.+?)\]", r'<span class="margin">[\1]</span>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    s = re.sub(r"\[\^(\w+)\]", r'<sup class="fn">\1</sup>', s)
    s = s.replace("[?]", '<span class="doubt">[?]</span>')
    return s


def table(rows):
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    cells = [r for r in cells if not all(re.fullmatch(r":?-+:?", c or "-") for c in r)]
    if not cells:
        return ""
    out = ["<table>"]
    for i, r in enumerate(cells):
        tag = "th" if i == 0 else "td"
        out.append("<tr>" + "".join(f"<{tag}>{inline(c)}</{tag}>" for c in r) + "</tr>")
    out.append("</table>")
    return "\n".join(out)


def renumber(md: str) -> str:
    """Number footnotes 1, 2, 3 ... in the order they first appear in the text."""
    order = []
    for k in re.findall(r"\[\^(\w+)\](?!:)", md):
        if k not in order:
            order.append(k)
    new = {k: str(i + 1) for i, k in enumerate(order)}
    return re.sub(r"\[\^(\w+)\]", lambda m: "[^" + new.get(m.group(1), m.group(1)) + "]", md)


def convert(md: str, sections: list, front: bool = False) -> str:
    """Markdown subset -> HTML. Each '# ' heading opens a new <section> with its own running head."""
    lines = md.replace("\r", "").split("\n")
    notes = {}
    body = []
    for ln in lines:                      # pull footnote definitions out
        m = re.match(r"\[\^(\w+)\]:\s*(.*)", ln)
        if m:
            notes[m.group(1)] = m.group(2)
            last = m.group(1)
        elif notes and ln.startswith("    ") and body and body[-1] is None:
            notes[last] += " " + ln.strip()
        else:
            body.append(ln)
            continue
        body.append(None)
    lines = [l for l in body if l is not None]

    out, i, open_sec, used = [], 0, False, []

    def close():
        nonlocal open_sec
        if open_sec:
            mine = [k for k in used if k in notes]
            if mine:
                out.append('<div class="notes"><div class="notes-h">Notes</div>')
                for k in mine:
                    out.append(f'<p><sup>{html.escape(k)}</sup> {inline(notes[k])}</p>')
                out.append("</div>")
            used.clear()
            out.append("</section>")
            open_sec = False

    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        for k in re.findall(r"\[\^(\w+)\]", ln):
            if k not in used:
                used.append(k)
        if ln.startswith("# "):
            close()
            title = ln[2:].strip()
            n = len(sections)
            sections.append(re.sub(r"\[\^\w+\]|[*_]", "", title).strip())
            cls = "front" if front else "chapter"
            out.append(f'<section class="{cls}" style="page: s{n}">')
            out.append(f'<h1 id="s{n}">{inline(title)}</h1>')
            open_sec = True
            # Latin title line in italics directly under the heading
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and re.fullmatch(r"\*[^*].*\*", lines[j].strip()):
                out.append(f'<p class="latin-title">{inline(lines[j].strip())}</p>')
                i = j
            out.append(FLEURON)
        elif ln.startswith("### "):
            out.append(f"<h3>{inline(ln[4:].strip())}</h3>")
        elif ln.startswith("## "):
            out.append(f"<h2>{inline(ln[3:].strip())}</h2>")
        elif ln.startswith("|") and i + 1 < len(lines) and re.match(r"\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            j = i
            while j < len(lines) and lines[j].startswith("|"):
                j += 1
            out.append(table(lines[i:j]))
            i = j - 1
        elif ln.startswith("|"):
            j, st = i, []
            while j < len(lines) and lines[j].startswith("|"):
                st.append(inline(lines[j][1:].strip()))
                j += 1
            out.append('<p class="verse">' + "<br>\n".join(st) + "</p>")
            i = j - 1
        elif ln.startswith("- "):
            j, items = i, []
            while j < len(lines) and lines[j].startswith("- "):
                items.append(f"<li>{inline(lines[j][2:].strip())}</li>")
                j += 1
            out.append("<ul>" + "\n".join(items) + "</ul>")
            i = j - 1
        elif ln.startswith("> "):
            out.append(f'<p class="center">{inline(ln[2:].strip())}</p>')
        elif ln.strip() == "---":
            out.append(FLEURON)
        else:
            j, para = i, []
            while j < len(lines) and lines[j].strip() and not re.match(r"(#|\||- |> )", lines[j]):
                para.append(lines[j].strip())
                j += 1
            text = " ".join(para)
            cls = ' class="latin"' if re.fullmatch(r"\*[^*].*\*", text) else ""
            out.append(f"<p{cls}>{inline(text)}</p>")
            i = j - 1
        i += 1
    close()
    return "\n".join(out)


CSS = """
@page { size: 6.14in 9.21in; margin: 0.95in 0.8in 0.9in 0.8in;
  @bottom-center { content: counter(page); font-family: Palatino, 'Palatino Linotype', serif; font-size: 9.5pt; } }
@page :first { @bottom-center { content: none; } @top-center { content: none; } }
@page plain { @bottom-center { content: none; } @top-center { content: none; } }
html { font-family: Palatino, 'Palatino Linotype', 'Book Antiqua', serif; font-size: 11pt; line-height: 1.42; color: #111; }
body { margin: 0; }
p { margin: 0 0 0.62em 0; text-align: justify; hyphens: auto; orphans: 3; widows: 3; }
h1, h2, h3 { color: #b3261e; font-weight: bold; text-align: center; break-after: avoid; hyphens: none; }
h1 { font-size: 17pt; line-height: 1.25; margin: 0.6in 0 0.25em 0; }
h2 { font-size: 12.5pt; line-height: 1.3; margin: 1.5em 0 0.55em 0; }
h3 { font-size: 10.5pt; font-style: italic; font-weight: normal; margin: 1em 0 0.4em 0; }
section { break-before: page; }
.latin-title { text-align: center; font-style: italic; margin-bottom: 0.2em; }
p.latin { text-align: center; font-style: italic; }
p.center { text-align: center; }
.fleuron { text-align: center; margin: 0.7em 0 1.1em 0; font-family: 'Apple Symbols', 'Hoefler Text', Palatino, serif; color: #333; break-after: avoid; }
p.verse { text-align: left; margin: 0 0 0.75em 1.6em; break-inside: avoid; hyphens: none; }
.pg { color: #9a6a64; font-size: 7.5pt; vertical-align: 0.25em; padding: 0 0.15em; font-style: normal; font-weight: normal; }
.margin { font-size: 8.5pt; font-style: italic; color: #555; }
.doubt { color: #b3261e; font-size: 8pt; }
sup.fn { font-size: 7pt; color: #b3261e; line-height: 0; }
.notes { break-inside: avoid; margin-top: 1.6em; border-top: 0.5pt solid #999; padding-top: 0.5em; font-size: 9pt; line-height: 1.32; }
.notes p { text-align: left; margin-bottom: 0.35em; break-inside: avoid; }
.notes-h { break-after: avoid; }
.notes-h { font-variant: small-caps; letter-spacing: 0.06em; margin-bottom: 0.3em; }
table { border-collapse: collapse; margin: 0.5em auto 1em auto; font-size: 8.6pt; line-height: 1.25; width: 100%; }
th { font-weight: normal; font-variant: small-caps; border-bottom: 0.5pt solid #555; text-align: left; padding: 2pt 4pt; }
td { padding: 1.3pt 4pt; vertical-align: top; border-bottom: 0.25pt solid #ddd; }
tr { break-inside: avoid; }
ul { list-style: none; padding: 0; margin: 0 0 0.8em 0; }
li { margin: 0 0 0.3em 1.4em; text-indent: -1.4em; text-align: left; }
/* front pages */
.plainpage { page: plain; break-before: page; text-align: center; }
.plainpage p { text-align: center; hyphens: none; }
.half { padding-top: 2.2in; }
.half .t { font-size: 25pt; font-weight: bold; letter-spacing: 0.04em; line-height: 1.2; }
.tp .t1 { font-size: 23pt; font-weight: bold; letter-spacing: 0.05em; margin-top: 0.45in; }
.tp .t2 { font-size: 13pt; font-weight: bold; color: #b3261e; letter-spacing: 0.06em; }
.tp .it { font-style: italic; }
.tp .au { font-size: 15pt; font-weight: bold; margin: 0.2em 0; }
.tp .sm { font-size: 10pt; }
.cr { padding-top: 1.6in; font-style: italic; font-size: 9.6pt; }
.cr p { margin-bottom: 1.5em; }
.toc { list-style: none; padding: 0; }
.toc li { display: flex; margin: 0 0 0.34em 0; text-indent: 0; }
.toc li span.d { flex: 1; border-bottom: 0.5pt dotted #777; margin: 0 0.4em 0.32em 0.4em; }
.toc li.sub { margin-left: 1.3em; }
"""


SHORT = {  # running heads for the sections whose full titles are too long for one line
    "VI.": "VI. On the Passion of Christ",
    "VII.": "VII. On the Resurrection and Ascension of Christ",
    "XII.": "XII. Under Persecution, against Enemies",
    "XIII.": "XIII. Against the Tyranny and Snares of Satan",
    "XIV.": "XIV. Thanksgiving for Benefits",
    "XV.": "XV. In Sickness and the Agony of Death",
    "XVII.": "XVII. Morning and Evening",
    "IX.": "IX. For Those Coming to the Holy Supper",
}


def page_rules(sections):
    rules = []
    for n, t in enumerate(sections):
        t = SHORT.get(t.split(" ")[0], t)
        t = t.replace("\\", "").replace('"', "'")
        rules.append(
            f"@page s{n} {{ @top-center {{ content: \"{t}\"; font-family: Palatino, 'Palatino Linotype', serif; "
            "font-size: 8.8pt; font-variant: small-caps; letter-spacing: 0.09em; color: #333; } }\n"
            f"@page s{n}:first {{ @top-center {{ content: none; }} }}")
    return "\n".join(rules)


def render(toc_pages=None):
    sections = []
    front = FRONT.read_text(encoding="utf-8")
    parts = []
    note = NOTE
    if note.exists():
        parts.append(convert(note.read_text(encoding="utf-8"), sections, front=True))
    n_front = len(sections)
    for f in sorted(SRC.glob("*.md")):
        parts.append(convert(renumber(f.read_text(encoding="utf-8")), sections))
    toc = ['<section class="front" style="page: toc"><h1>Contents</h1>', FLEURON, '<ul class="toc">']
    for n, t in enumerate(sections):
        pg = (toc_pages or {}).get(n, "")
        toc.append(f'<li><span>{html.escape(t)}</span><span class="d"></span><span>{pg}</span></li>')
    toc.append("</ul></section>")
    doc = ("<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
           f"<title>Andreas Musculus, Precationes ({EDITION}) — English</title>"
           f"<style>{CSS}\n@page toc {{ @top-center {{ content: none; }} }}\n{page_rules(sections)}</style></head><body>"
           + front + "\n".join(toc) + "\n".join(parts) + "</body></html>")
    OUT.mkdir(exist_ok=True)
    (OUT / "book.html").write_text(doc, encoding="utf-8")
    PDF.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={PDF}", (OUT / "book.html").as_uri()],
                   check=True, capture_output=True, timeout=600)
    return sections


def find_pages(sections):
    """Read the PDF back and find the page each section heading starts on."""
    txt = subprocess.run(["pdftotext", "-layout", str(PDF), "-"], capture_output=True, text=True).stdout
    pages = txt.split("\f")
    norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
    found, start = {}, 0
    for n, t in enumerate(sections):
        key = norm(t)[:38]
        for p in range(start, len(pages)):
            head = norm("".join(pages[p].split("\n")[:9]))
            if key and key in head and "contents" not in head[:12]:
                found[n] = p + 1
                start = p
                break
    return found, len(pages)


if __name__ == "__main__":
    secs = render()
    pages, total = find_pages(secs)
    secs = render(pages)                       # second pass: contents with page numbers
    pages2, total = find_pages(secs)
    missing = [secs[n] for n in range(len(secs)) if n not in pages2]
    print(f"sections: {len(secs)}  pages: {total}  ->  {PDF}")
    if pages2 != pages:
        print("note: page numbers moved between passes; run again")
    if missing:
        print("contents entries without a page:", missing)
