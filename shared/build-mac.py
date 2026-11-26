#!/usr/bin/env python3
"""macOS build for a Scholastic Lutherans volume: Markdown -> HTML (pandoc) -> PDF (Chrome headless).

Usage:  python3 shared/build-mac.py <volume-dir>

The volume directory holds a `build.json`:

    {
      "stem":   "Author-Title-Year-English-Scholastic-Lutherans",   # PDF name in review/
      "title":  "Author, Title (Year) — English",                   # PDF document title
      "front":  "review/front.html",                                # half-title, title page, copyright page
      "parts":  ["review/front/*.md", "review/parts/*.md"],         # Markdown, in order (globs are sorted)
      "master": "review/<work-slug>.md",                            # assembled master file (written on every build)
      "toc_depth": 2,                                               # heading levels in the contents (1 or 2)
      "short_heads": {"Long Section Title": "Short Running Head"}   # optional
    }

House format: 6.14 x 9.21 in, Palatino 11 pt, red headings, small-caps running head, page number at the foot.
Footnotes written as [^key] become one endnote apparatus at the end of the volume.
`<!-- p.N -->` page marks stay in the master file and are invisible in the PDF.
Needs: pandoc, Google Chrome, poppler (pdftotext).
"""
import glob, html, json, re, subprocess, sys
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = """
@page { size: 6.14in 9.21in; margin: 0.95in 0.8in 0.9in 0.8in;
  @bottom-center { content: counter(page); font-family: Palatino, 'Palatino Linotype', serif; font-size: 9.5pt; } }
@page :first { @bottom-center { content: none; } @top-center { content: none; } }
@page plain { @bottom-center { content: none; } @top-center { content: none; } }
@page toc { @top-center { content: none; } }
html { font-family: Palatino, 'Palatino Linotype', 'Book Antiqua', 'Times New Roman', serif; font-size: 11pt; line-height: 1.42; color: #111; }
body { margin: 0; }
p { margin: 0 0 0.62em 0; text-align: justify; hyphens: auto; orphans: 3; widows: 3; }
h1, h2, h3, h4 { color: #b3261e; font-weight: bold; text-align: center; break-after: avoid; hyphens: none; }
h1 { font-size: 18pt; line-height: 1.25; margin: 0.55in 0 0.7em 0; }
h2 { font-size: 13.5pt; line-height: 1.3; margin: 1.6em 0 0.6em 0; }
h3 { font-size: 11.5pt; line-height: 1.3; margin: 1.3em 0 0.5em 0; }
h4 { font-size: 11pt; font-style: italic; font-weight: normal; margin: 1em 0 0.4em 0; }
section.level1 { break-before: page; }
blockquote { margin: 0 0 0.7em 1.5em; padding: 0; }
blockquote p { text-align: left; hyphens: none; margin-bottom: 0.35em; }
ol, ul { margin: 0 0 0.7em 0; padding-left: 1.5em; }
li { margin-bottom: 0.25em; text-align: left; }
li p { text-align: left; margin-bottom: 0.25em; }
p.fleuron { text-align: center; margin: 0.9em 0 1.1em 0; color: #b3261e; break-after: avoid; }
a { color: inherit; text-decoration: none; }
sup, a.footnote-ref { font-size: 7pt; color: #b3261e; line-height: 0; }
section.footnotes { break-before: page; font-size: 9.2pt; line-height: 1.34; page: notes; }
section.footnotes hr { display: none; }
section.footnotes ol { padding-left: 2.2em; }
section.footnotes li { margin-bottom: 0.45em; }
section.footnotes li p { text-align: left; hyphens: auto; }
a.footnote-back { display: none; }
table { border-collapse: collapse; margin: 0.5em auto 1em auto; font-size: 8.8pt; line-height: 1.25; width: 100%; }
th { font-weight: normal; font-variant: small-caps; border-bottom: 0.5pt solid #555; text-align: left; padding: 2pt 4pt; }
td { padding: 1.3pt 4pt; vertical-align: top; border-bottom: 0.25pt solid #ddd; }
tr { break-inside: avoid; }
.plainpage { page: plain; break-before: page; text-align: center; }
.plainpage p { text-align: center; hyphens: none; }
.half { padding-top: 2.0in; }
.half .t { font-size: 24pt; font-weight: bold; letter-spacing: 0.03em; line-height: 1.2; color: #b3261e; }
.tp .t1 { font-size: 21pt; font-weight: bold; letter-spacing: 0.03em; margin-top: 0.4in; color: #b3261e; line-height: 1.2; }
.tp .t2 { font-size: 14pt; font-weight: bold; }
.tp .it { font-style: italic; }
.tp .au { font-size: 14pt; font-weight: bold; margin: 0.2em 0; }
.tp .sm { font-size: 10pt; }
.tp .red, .half .red { color: #b3261e; }
.cr { padding-top: 1.5in; font-style: italic; font-size: 9.6pt; }
.cr p { margin-bottom: 1.4em; }
.toc { list-style: none; padding: 0; }
.toc li { display: flex; margin: 0 0 0.3em 0; }
.toc li span.d { flex: 1; border-bottom: 0.5pt dotted #777; margin: 0 0.4em 0.32em 0.4em; }
.toc li.l2 { margin-left: 1.3em; font-size: 10pt; }
"""

HEAD_FONT = ("font-family: Palatino, 'Palatino Linotype', serif; font-size: 8.8pt; "
             "font-variant: small-caps; letter-spacing: 0.09em; color: #333;")


def plain(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def render(vol, cfg, toc_pages=None):
    files = []
    for pat in cfg["parts"]:
        files += sorted(glob.glob(str(vol / pat)))
    md = "\n\n".join(Path(f).read_text(encoding="utf-8").strip() for f in files) + "\n"
    (vol / cfg["master"]).write_text(md, encoding="utf-8")
    body = subprocess.run(
        ["pandoc", "-f", "markdown+smart-implicit_figures", "-t", "html5", "--section-divs", "--wrap=none"],
        input=md, capture_output=True, text=True, check=True).stdout
    body = re.sub(r"<p>— ❦ —</p>", '<p class="fleuron">— ❦ —</p>', body)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    # endnote apparatus heading
    body = body.replace('<section id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">',
                        '<section id="footnotes" class="footnotes" role="doc-endnotes"><h1 id="endnotes">Endnotes</h1>')
    # running heads: one named page per level-1 section
    heads, rules, n = [], [], 0

    def tag(m):
        nonlocal n
        sid = m.group(1)
        n += 1
        return f'<section id="{sid}" class="level1" style="page: s{n}">'
    body = re.sub(r'<section id="([^"]+)" class="level1[^"]*">', tag, body)
    entries = []      # (level, title, anchor id)
    for m in re.finditer(r'<h([12])[^>]*>(.*?)</h\1>', body, re.S):
        lvl = int(m.group(1))
        if lvl <= cfg.get("toc_depth", 2):
            entries.append((lvl, plain(m.group(2)), ""))
    k = 0
    for lvl, title, _ in entries:
        if lvl == 1 and title != "Endnotes":
            k += 1
            t = cfg.get("short_heads", {}).get(title, title).replace("\\", "").replace('"', "'")
            rules.append(f'@page s{k} {{ @top-center {{ content: "{t}"; {HEAD_FONT} }} }}\n'
                         f'@page s{k}:first {{ @top-center {{ content: none; }} }}')
    rules.append(f'@page notes {{ @top-center {{ content: "Endnotes"; {HEAD_FONT} }} }}\n'
                 '@page notes:first { @top-center { content: none; } }')
    toc = ['<section class="level1" style="page: toc"><h1>Contents</h1><p class="fleuron">— ❦ —</p><ul class="toc">']
    for i, (lvl, title, _) in enumerate(entries):
        pg = (toc_pages or {}).get(i, "")
        toc.append(f'<li class="l{lvl}"><span>{html.escape(title)}</span><span class="d"></span><span>{pg}</span></li>')
    toc.append("</ul></section>")
    front = (vol / cfg["front"]).read_text(encoding="utf-8")
    doc = ("<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
           f"<title>{html.escape(cfg['title'])}</title><style>{CSS}\n" + "\n".join(rules) + "</style></head><body>"
           + front + "\n".join(toc) + body + "</body></html>")
    out = vol / "review" / "build"
    out.mkdir(parents=True, exist_ok=True)
    (out / "book.html").write_text(doc, encoding="utf-8")
    pdf = vol / "review" / (cfg["stem"] + ".pdf")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", (out / "book.html").as_uri()],
                   check=True, capture_output=True, timeout=1200)
    return entries, pdf


def find_pages(entries, pdf):
    txt = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True).stdout
    pages = txt.split("\f")
    norm = lambda s: re.sub(r"[^a-z0-9Ͱ-Ͽἀ-῿]", "", s.lower())
    found, start = {}, 0
    for i, (lvl, title, _) in enumerate(entries):
        key = norm(title)[:34]
        if not key:
            continue
        for p in range(start, len(pages)):
            text = norm(pages[p]) if lvl > 1 else norm("".join(pages[p].split("\n")[:10]))
            if key in text and not (p < 12 and "contents" in norm(pages[p])[:40]):
                found[i] = p + 1
                start = p
                break
    return found, len(pages) - 1


if __name__ == "__main__":
    vol = Path(sys.argv[1]).resolve()
    cfg = json.loads((vol / "build.json").read_text(encoding="utf-8"))
    entries, pdf = render(vol, cfg)
    pages, total = find_pages(entries, pdf)
    entries, pdf = render(vol, cfg, pages)
    pages2, total = find_pages(entries, pdf)
    if pages2 != pages:
        entries, pdf = render(vol, cfg, pages2)
        pages2, total = find_pages(entries, pdf)
    missing = [entries[i][1] for i in range(len(entries)) if i not in pages2]
    print(f"contents entries: {len(entries)}  pages: {total}  ->  {pdf}")
    if missing:
        print("contents entries without a page:", missing[:20])
