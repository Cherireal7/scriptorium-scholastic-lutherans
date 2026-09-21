"""KJV Scripture-conformance pass.

Scans a translation MD for inline italic Scripture quotes followed by a
parenthetical citation, e.g.:

    *For God so loved the world...* (John 3:16)

and replaces the quote text with the KJV wording. Multi-verse ranges are
concatenated. Apocryphal books are skipped (KJV canon only). Very short
italic snippets are treated as fragments and left alone.

Data source: bibleapi/bibleapi-bibles-json kjv.json (public domain KJV).
Fetch once to shared/kjv.json before running.

Usage:  python apply-kjv-pass.py <path/to/translation.md>

Prints a summary + writes changes back in place.
"""

from __future__ import annotations
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
KJV_PATH = REPO_ROOT / "shared" / "kjv.json"

# --- book index → canonical KJV name ---
KJV_BOOKS = [
    "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy",
    "Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel",
    "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles", "Ezra",
    "Nehemiah", "Esther", "Job", "Psalms", "Proverbs",
    "Ecclesiastes", "Song of Solomon", "Isaiah", "Jeremiah", "Lamentations",
    "Ezekiel", "Daniel", "Hosea", "Joel", "Amos",
    "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk",
    "Zephaniah", "Haggai", "Zechariah", "Malachi",
    "Matthew", "Mark", "Luke", "John", "Acts",
    "Romans", "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians",
    "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians",
    "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews",
    "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude",
    "Revelation",
]

# --- abbreviation → canonical name (used in citation labels) ---
ABBREV = {
    "Gen": "Genesis", "Exod": "Exodus", "Ex": "Exodus", "Lev": "Leviticus",
    "Num": "Numbers", "Deut": "Deuteronomy", "Josh": "Joshua",
    "Judg": "Judges", "Ruth": "Ruth",
    "1 Sam": "1 Samuel", "2 Sam": "2 Samuel", "1Sam": "1 Samuel", "2Sam": "2 Samuel",
    "1 Kgs": "1 Kings", "2 Kgs": "2 Kings", "1Kgs": "1 Kings", "2Kgs": "2 Kings",
    "1 Kings": "1 Kings", "2 Kings": "2 Kings",
    "1 Chr": "1 Chronicles", "2 Chr": "2 Chronicles",
    "1Chr": "1 Chronicles", "2Chr": "2 Chronicles",
    "Ezra": "Ezra", "Neh": "Nehemiah", "Esth": "Esther",
    "Job": "Job", "Ps": "Psalms", "Psa": "Psalms", "Psalm": "Psalms", "Psalms": "Psalms",
    "Prov": "Proverbs", "Eccl": "Ecclesiastes", "Eccles": "Ecclesiastes",
    "Song": "Song of Solomon", "Cant": "Song of Solomon",
    "Isa": "Isaiah", "Jer": "Jeremiah", "Lam": "Lamentations",
    "Ezek": "Ezekiel", "Dan": "Daniel",
    "Hos": "Hosea", "Joel": "Joel", "Amos": "Amos", "Obad": "Obadiah",
    "Jonah": "Jonah", "Mic": "Micah", "Nah": "Nahum", "Hab": "Habakkuk",
    "Zeph": "Zephaniah", "Hag": "Haggai", "Zech": "Zechariah", "Mal": "Malachi",
    "Matt": "Matthew", "Mt": "Matthew", "Mk": "Mark", "Mark": "Mark",
    "Lk": "Luke", "Luke": "Luke", "Jn": "John", "John": "John",
    "Acts": "Acts",
    "Rom": "Romans",
    "1 Cor": "1 Corinthians", "2 Cor": "2 Corinthians",
    "1Cor": "1 Corinthians", "2Cor": "2 Corinthians",
    "Gal": "Galatians", "Eph": "Ephesians", "Phil": "Philippians",
    "Col": "Colossians",
    "1 Thess": "1 Thessalonians", "2 Thess": "2 Thessalonians",
    "1Thess": "1 Thessalonians", "2Thess": "2 Thessalonians",
    "1 Tim": "1 Timothy", "2 Tim": "2 Timothy",
    "1Tim": "1 Timothy", "2Tim": "2 Timothy",
    "Tit": "Titus", "Titus": "Titus", "Phlm": "Philemon",
    "Heb": "Hebrews", "Jas": "James", "Jam": "James", "James": "James",
    "1 Pet": "1 Peter", "2 Pet": "2 Peter", "1Pet": "1 Peter", "2Pet": "2 Peter",
    "1 John": "1 John", "2 John": "2 John", "3 John": "3 John",
    "1John": "1 John", "2John": "2 John", "3John": "3 John",
    "Jude": "Jude",
    "Rev": "Revelation", "Apoc": "Revelation",
}

# Apocryphal — outside KJV canon, skip
APOCRYPHA = {"Sir", "Sirach", "Wisd", "Wis", "Tob", "Tobit", "Jud", "Judith",
             "1 Macc", "2 Macc", "1Macc", "2Macc", "Ecclus", "Bar", "Baruch",
             "1 Esdr", "2 Esdr", "4 Esdr", "Esdr", "Sus", "Bel"}


def load_kjv() -> Dict[Tuple[str, int, int], str]:
    """Return (book_name, chapter, verse) → text."""
    data = json.loads(KJV_PATH.read_text(encoding="utf-8"))
    idx: Dict[Tuple[str, int, int], str] = {}
    for row in data["resultset"]["row"]:
        _id, book_num, chapter, verse, text = row["field"]
        book_name = KJV_BOOKS[book_num - 1]
        idx[(book_name, chapter, verse)] = text
    return idx


def lookup(kjv: Dict, book: str, chap: int, verses: List[int]) -> str | None:
    parts = []
    for v in verses:
        text = kjv.get((book, chap, v))
        if text is None:
            return None
        parts.append(text.strip())
    return " ".join(parts)


# Citation pattern: *quote* (Book Ch:v) or (Book Ch:v-v) or (Book Ch:v, v)
# The italic quote is the immediately-preceding *...* block.
# Balduin uses semicolons for composite (Book Ch:v; Book Ch:v) — skip those.
# Also skip stripe of format "(Book1 Ch:v; Book2 Ch:v)".

# Book-name alternatives (longest first for greedy match)
BOOK_ALTS = sorted(set(ABBREV.keys()) | APOCRYPHA, key=lambda s: -len(s))
BOOK_RE = r"(?:" + "|".join(re.escape(b) for b in BOOK_ALTS) + r")"

# match: * ... * ( Book [.] Ch:v[-v | , v]* )
# non-greedy on italic body; require it to end just before the citation paren
CITE_RE = re.compile(
    r"\*([^*\n][^*]{4,600}?[^*])\*\s*"           # italic quote  (no newlines inside quote)
    r"\((" + BOOK_RE + r")\.?\s*"                 # book
    r"(\d+)\s*[:.]\s*"                            # chapter
    r"(\d+(?:\s*[-–]\s*\d+)?"                     # verse (or range)
    r"(?:\s*,\s*\d+)*)"                           # or comma-list
    r"\)",
    flags=re.DOTALL,
)


def parse_verses(spec: str) -> List[int] | None:
    """'5' → [5]; '5-8' → [5,6,7,8]; '5, 7' → [5,7]. None if malformed."""
    spec = spec.replace("–", "-").strip()
    result: List[int] = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            try:
                lo, hi = map(int, part.split("-", 1))
            except ValueError:
                return None
            if hi < lo or hi - lo > 15:
                return None
            result.extend(range(lo, hi + 1))
        else:
            try:
                result.append(int(part))
            except ValueError:
                return None
    return result


def apply(md_path: Path) -> None:
    kjv = load_kjv()
    text = md_path.read_text(encoding="utf-8")

    replaced = 0
    skipped_apoc = 0
    skipped_frag = 0
    skipped_composite = 0
    skipped_lookup_miss = 0

    def repl(m: re.Match) -> str:
        nonlocal replaced, skipped_apoc, skipped_frag, skipped_composite, skipped_lookup_miss
        quote, book_raw, chap_str, verse_spec = m.group(1), m.group(2), m.group(3), m.group(4)

        # composite? If the character *after* the whole match is nothing (end
        # of paren) that's fine — CITE_RE already excluded semicolons.
        if ";" in m.group(0):
            skipped_composite += 1
            return m.group(0)

        if book_raw in APOCRYPHA:
            skipped_apoc += 1
            return m.group(0)

        book = ABBREV.get(book_raw)
        if not book:
            skipped_lookup_miss += 1
            return m.group(0)

        try:
            chap = int(chap_str)
        except ValueError:
            skipped_lookup_miss += 1
            return m.group(0)

        verses = parse_verses(verse_spec)
        if not verses:
            skipped_lookup_miss += 1
            return m.group(0)

        kjv_text = lookup(kjv, book, chap, verses)
        if kjv_text is None:
            skipped_lookup_miss += 1
            return m.group(0)

        # Fragment check: if the original quote is much shorter than KJV,
        # Balduin was quoting a snippet — preserve it (don't overwrite).
        orig_len = len(quote.strip())
        kjv_len = len(kjv_text)
        if orig_len < 40 or orig_len < 0.5 * kjv_len:
            skipped_frag += 1
            return m.group(0)

        replaced += 1
        return f"*{kjv_text}* ({book_raw} {chap_str}:{verse_spec})"

    new_text = CITE_RE.sub(repl, text)

    if new_text == text:
        print("No changes made.")
    else:
        md_path.write_text(new_text, encoding="utf-8", newline="\n")

    print(f"Replaced:            {replaced}")
    print(f"Skipped (apocrypha): {skipped_apoc}")
    print(f"Skipped (fragment):  {skipped_frag}")
    print(f"Skipped (composite): {skipped_composite}")
    print(f"Skipped (miss):      {skipped_lookup_miss}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: apply-kjv-pass.py <translation.md>", file=sys.stderr)
        sys.exit(2)
    apply(Path(sys.argv[1]))
