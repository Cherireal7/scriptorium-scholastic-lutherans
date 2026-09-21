"""Second-pass Scripture-conformance sweep: expand *fragment* quotes that
are actually shortened KJV quotes (as opposed to genuine paraphrases of the
Vulgate).

For each italic Scripture citation the first-pass KJV script preserved
(because the quote was <50% of the full KJV verse), compute the Jaccard
similarity of *content* words between the italic quote and the KJV verse.
If content overlap is high, the quote is a shortened KJV quote and we
expand it to full KJV wording. If overlap is low, the quote is a genuine
paraphrase (probably tracking the Vulgate or Balduin's own gloss) and we
leave it alone.

Usage:  python expand-fragment-scriptures.py <path/to/translation.md> [--threshold 0.6]
"""

from __future__ import annotations
import argparse
import json
import re
import string
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
KJV_PATH = REPO_ROOT / "shared" / "kjv.json"

# Reuse the same book maps as the first-pass script
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
APOCRYPHA = {"Sir", "Sirach", "Wisd", "Wis", "Tob", "Tobit", "Jud", "Judith",
             "1 Macc", "2 Macc", "1Macc", "2Macc", "Ecclus", "Bar", "Baruch"}

STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "if", "of", "to", "in", "on", "at",
    "by", "for", "with", "from", "as", "is", "are", "was", "were", "be",
    "been", "being", "am", "he", "she", "it", "his", "her", "its", "him",
    "them", "they", "their", "we", "us", "our", "you", "your", "i", "me",
    "my", "mine", "thee", "thou", "thy", "thine", "ye",
    "shall", "will", "would", "should", "may", "might", "can", "could",
    "do", "does", "did", "have", "has", "had", "not", "no", "so", "that",
    "this", "these", "those", "which", "who", "whom", "what", "when",
    "where", "why", "how", "there", "here", "then", "than", "such", "some",
    "any", "all", "every", "each", "unto", "against", "before", "after",
    "into", "upon", "out", "up", "down", "over", "under", "through",
    "one", "two", "many", "much", "more", "most", "own",
    "s",
}

BOOK_ALTS = sorted(set(ABBREV.keys()) | APOCRYPHA, key=lambda s: -len(s))
BOOK_RE = r"(?:" + "|".join(re.escape(b) for b in BOOK_ALTS) + r")"

CITE_RE = re.compile(
    r"\*([^*\n][^*]{4,600}?[^*])\*\s*"
    r"\((" + BOOK_RE + r")\.?\s*"
    r"(\d+)\s*[:.]\s*"
    r"(\d+(?:\s*[-–]\s*\d+)?"
    r"(?:\s*,\s*\d+)*)"
    r"\)",
    flags=re.DOTALL,
)


def load_kjv() -> Dict[Tuple[str, int, int], str]:
    data = json.loads(KJV_PATH.read_text(encoding="utf-8"))
    idx: Dict[Tuple[str, int, int], str] = {}
    for row in data["resultset"]["row"]:
        _id, book_num, chapter, verse, text = row["field"]
        book_name = KJV_BOOKS[book_num - 1]
        idx[(book_name, chapter, verse)] = text
    return idx


def parse_verses(spec: str) -> List[int] | None:
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


def content_words(s: str) -> Set[str]:
    """Lowercase, strip punctuation, remove stopwords, drop tokens < 3 chars."""
    s = s.lower()
    # remove punctuation
    s = s.translate(str.maketrans("", "", string.punctuation + "—–"))
    tokens = s.split()
    return {t for t in tokens if len(t) >= 3 and t not in STOPWORDS}


def jaccard(a: Set[str], b: Set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def apply(md_path: Path, threshold: float) -> None:
    kjv = load_kjv()
    text = md_path.read_text(encoding="utf-8")

    expanded = 0
    kept_paraphrase = 0
    kept_full = 0  # already at/above 50% of KJV; leave for first-pass script
    skipped_apoc = 0
    skipped_composite = 0
    skipped_miss = 0

    def repl(m: re.Match) -> str:
        nonlocal expanded, kept_paraphrase, kept_full
        nonlocal skipped_apoc, skipped_composite, skipped_miss

        quote, book_raw, chap_str, verse_spec = m.group(1), m.group(2), m.group(3), m.group(4)

        if ";" in m.group(0):
            skipped_composite += 1
            return m.group(0)

        if book_raw in APOCRYPHA:
            skipped_apoc += 1
            return m.group(0)

        book = ABBREV.get(book_raw)
        if not book:
            skipped_miss += 1
            return m.group(0)

        try:
            chap = int(chap_str)
        except ValueError:
            skipped_miss += 1
            return m.group(0)

        verses = parse_verses(verse_spec)
        if not verses:
            skipped_miss += 1
            return m.group(0)

        parts = []
        for v in verses:
            t = kjv.get((book, chap, v))
            if t is None:
                skipped_miss += 1
                return m.group(0)
            parts.append(t.strip())
        kjv_text = " ".join(parts)

        # If the italic is already ≥50% of full KJV, this is a case the
        # first-pass script would have handled; don't second-guess.
        if len(quote.strip()) >= 0.5 * len(kjv_text):
            kept_full += 1
            return m.group(0)

        # Content-word overlap
        q_words = content_words(quote)
        k_words = content_words(kjv_text)
        sim = jaccard(q_words, k_words)

        if sim >= threshold:
            expanded += 1
            return f"*{kjv_text}* ({book_raw} {chap_str}:{verse_spec})"
        else:
            kept_paraphrase += 1
            return m.group(0)

    new_text = CITE_RE.sub(repl, text)

    if new_text == text:
        print("No changes made.")
    else:
        md_path.write_text(new_text, encoding="utf-8", newline="\n")

    print(f"Expanded (fragment -> full KJV):  {expanded}")
    print(f"Kept (already full):           {kept_full}")
    print(f"Kept (genuine paraphrase):     {kept_paraphrase}")
    print(f"Skipped (apocrypha):           {skipped_apoc}")
    print(f"Skipped (composite):           {skipped_composite}")
    print(f"Skipped (miss):                {skipped_miss}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("md_path", type=Path)
    parser.add_argument("--threshold", type=float, default=0.5,
                        help="Jaccard content-word overlap needed to expand (default 0.5)")
    args = parser.parse_args()
    apply(args.md_path, args.threshold)
