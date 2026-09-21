"""Build Scripture and Fathers indices for a Scholastic Lutherans translation MD.

Scans the finished English MD, tracks (Liber, Cap, Casus) context per line, and
extracts:

  1. Scripture citations of the form  (Book Ch:v[-v]).
  2. Named Church Fathers, classical authors, and cited theologians.

Emits two Markdown-formatted indices ready for direct concatenation to the
volume MD as back-matter (after the body's closing doxology).

Location scheme: `L.C.S` (Liber.Chapter.Casus, all Roman); if no Casus in
context, just `L.C`.

Usage:  python build-indices.py <path/to/translation.md> [output.md]

If no output path is given, writes to stdout.
"""

from __future__ import annotations
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import DefaultDict, Set, Tuple

# --- book aliases (same as apply-kjv-pass.py, plus apocrypha) ---
CANON_ORDER = [
    "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy",
    "Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel",
    "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles", "Ezra",
    "Nehemiah", "Esther", "Job", "Psalms", "Proverbs",
    "Ecclesiastes", "Song of Solomon", "Isaiah", "Jeremiah", "Lamentations",
    "Ezekiel", "Daniel", "Hosea", "Joel", "Amos",
    "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk",
    "Zephaniah", "Haggai", "Zechariah", "Malachi",
    "Wisdom", "Sirach", "Tobit", "Judith", "Baruch", "1 Maccabees", "2 Maccabees",
    "Matthew", "Mark", "Luke", "John", "Acts",
    "Romans", "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians",
    "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians",
    "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews",
    "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude",
    "Revelation",
]
CANON_ORDER_MAP = {name: i for i, name in enumerate(CANON_ORDER)}

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
    "Sir": "Sirach", "Sirach": "Sirach", "Ecclus": "Sirach",
    "Wisd": "Wisdom", "Wis": "Wisdom", "Wisdom": "Wisdom",
    "Tob": "Tobit", "Tobit": "Tobit", "Jud": "Judith", "Judith": "Judith",
    "Bar": "Baruch", "Baruch": "Baruch",
    "1 Macc": "1 Maccabees", "2 Macc": "2 Maccabees",
    "1Macc": "1 Maccabees", "2Macc": "2 Maccabees",
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

# Named authorities Balduin cites frequently. Deliberately curated: Church
# Fathers, prominent medieval Scholastics, Reformers, and a handful of
# classical authors he engages by name. Roman numerals stripped from surface
# forms so "Gregory VII" collates with "Gregory the Great" only if we merge.
FATHERS = [
    # Apostolic + ante-Nicene
    "Ignatius", "Irenaeus", "Justin Martyr", "Justin", "Tertullian", "Cyprian",
    "Origen", "Clement of Alexandria", "Clement",
    # Nicene / Post-Nicene Greek
    "Athanasius", "Basil", "Gregory Nazianzen", "Gregory of Nyssa",
    "Chrysostom", "John Chrysostom", "Epiphanius", "Theodoret", "Theodore",
    "Eusebius", "Cyril of Alexandria", "Cyril of Jerusalem", "Cyril",
    # Latin
    "Ambrose", "Jerome", "Augustine", "Leo", "Gregory the Great", "Gregory",
    "Prosper", "Cassian", "John Cassian", "Isidore", "Bede",
    # Byzantine / later Greek
    "John Damascene", "Damascene", "Nicephorus",
    # Medieval Latin scholastics
    "Anselm", "Bernard", "Bernard of Clairvaux", "Peter Lombard", "Lombard",
    "Thomas", "Thomas Aquinas", "Aquinas", "Bonaventure", "Duns Scotus",
    "Scotus", "William of Ockham", "Ockham", "Marsilius", "Gabriel Biel",
    "Biel",
    # Byzantine / Eastern
    "Photius", "Nicetas", "Nicholas of Cusa",
    # Reformers
    "Luther", "Melanchthon", "Chemnitz", "Brenz", "Calvin", "Beza",
    "Zwingli", "Bullinger", "Peter Martyr",
    # Lutheran orthodoxy contemporaries
    "Gerhard", "Meisner", "Hutter", "Leonhard Hutter", "Selnecker",
    "Kirchner", "Buchner", "Balduin",
    # Roman Catholic controversialists (Balduin engages heavily)
    "Bellarmine", "Suárez", "Suarez", "Mariana", "Gregory de Valentia",
    "Valentia", "Alvarus Pelagius", "Alvarus", "Panormitanus",
    "Silvester Prierias", "Silvester", "Bozius", "Barclay",
    "William Barclay", "Azorius", "Loricchius", "Iacobus Loricchius",
    "Domingo Soto", "Dominicus Soto", "Cajetan", "Trent",
    "Council of Trent", "Trident",
    # Councils frequently mentioned
    "Nicene Council", "Council of Nicaea", "Nicaea", "Chalcedon",
    "Constantinople", "Ephesus", "Laodicea", "Elvira", "Arelate",
    # Classical
    "Cicero", "Aristotle", "Plato", "Seneca", "Horace", "Ovid", "Livy",
    "Plutarch", "Herodotus", "Xenophon", "Lactantius", "Boethius",
    "Josephus", "Plautus", "Martial", "Virgil", "Vergil",
    # Heretics named by Balduin
    "Arius", "Nestorius", "Eutyches", "Pelagius", "Manichaeus",
    "Montanus", "Marcion", "Photinus", "Sabellius", "Macedonius",
    # Others
    "Erasmus", "Sleidan", "Vincent",
]

# Sort by length descending so multi-word matches take precedence
FATHERS_SORTED = sorted(set(FATHERS), key=lambda s: -len(s))

# --- context tracking regexes ---
LIBER_RE = re.compile(r"^#\s+Liber\s+([IVXL]+)\b", re.IGNORECASE)
CHAPTER_RE = re.compile(r"^##\s+Chapter\s+([IVXL]+)\b", re.IGNORECASE)
CASUS_RE = re.compile(r"^###\s+Casus\s+([IVXL]+)\b", re.IGNORECASE)

# --- citation regex ---
CITE_BOOKS = sorted(set(ABBREV.keys()), key=lambda s: -len(s))
CITE_RE = re.compile(
    r"\((" + "|".join(re.escape(b) for b in CITE_BOOKS) + r")\.?\s+"
    r"(\d+)\s*[:.]\s*"
    r"(\d+(?:\s*[-–]\s*\d+)?(?:\s*,\s*\d+)*)"
    r"\)"
)

# --- fathers regex (word-bounded, case-sensitive to catch proper nouns) ---
FATHER_RE = re.compile(
    r"(?<![A-Za-z])(" + "|".join(re.escape(f) for f in FATHERS_SORTED) + r")(?![A-Za-z])"
)


def normalize_verse(spec: str) -> str:
    return spec.replace("–", "-").replace(" ", "")


def format_location(liber: str | None, chap: str | None, casus: str | None) -> str | None:
    parts = [p for p in (liber, chap, casus) if p]
    if not parts:
        return None
    return ".".join(parts)


def build(md_path: Path) -> str:
    scripture: DefaultDict[Tuple[int, str], Set[Tuple[int, str]]] = defaultdict(set)
    # scripture: (canon_order, verse_key) -> {(sort_key, location_display), ...}
    fathers: DefaultDict[str, Set[str]] = defaultdict(set)

    liber = chap = casus = None
    front_matter = True

    for lineno, line in enumerate(md_path.read_text(encoding="utf-8").splitlines(), start=1):
        m = LIBER_RE.match(line)
        if m:
            liber = m.group(1).upper()
            chap = casus = None
            front_matter = False
            continue
        m = CHAPTER_RE.match(line)
        if m:
            chap = m.group(1).upper()
            casus = None
            continue
        m = CASUS_RE.match(line)
        if m:
            casus = m.group(1).upper()
            continue

        if front_matter:
            continue

        loc = format_location(liber, chap, casus)
        if not loc:
            continue

        # scripture
        for cm in CITE_RE.finditer(line):
            book_raw, chap_num, verse_spec = cm.group(1), cm.group(2), cm.group(3)
            book = ABBREV.get(book_raw)
            if not book:
                continue
            verse_key = f"{chap_num}:{normalize_verse(verse_spec)}"
            canon_idx = CANON_ORDER_MAP.get(book, 999)
            scripture[(canon_idx, book)].add((verse_key_sort(verse_key), verse_key, loc))

        # fathers — case sensitive
        for fm in FATHER_RE.finditer(line):
            name = fm.group(1)
            fathers[name].add(loc)

    return render(scripture, fathers)


def verse_key_sort(vk: str) -> Tuple[int, int]:
    """Sort '3:16' before '3:17' before '10:1'."""
    ch, v = vk.split(":", 1)
    v_head = re.match(r"\d+", v)
    v_num = int(v_head.group()) if v_head else 0
    return (int(ch), v_num)


def location_sort(loc: str) -> Tuple[int, int, int]:
    roman_map = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7,
                 "VIII": 8, "IX": 9, "X": 10, "XI": 11, "XII": 12, "XIII": 13,
                 "XIV": 14, "XV": 15, "XVI": 16, "XVII": 17, "XVIII": 18,
                 "XIX": 19, "XX": 20}
    parts = loc.split(".")
    key = [roman_map.get(p, 99) for p in parts]
    while len(key) < 3:
        key.append(0)
    return tuple(key[:3])


def render(scripture, fathers) -> str:
    out = []
    out.append("")
    out.append("```{=openxml}")
    out.append('<w:br w:type="page"/>')
    out.append("```")
    out.append("")
    out.append("# Index I. Scripture Citations")
    out.append("")
    out.append("*References give the location within the volume as L.C.S — "
               "Liber (I–IV), Chapter (I–XVIII in Liber IV, etc.), Casus. "
               "Where no Casus is listed, the citation falls in the chapter "
               "preamble or general discussion.*")
    out.append("")

    for (canon_idx, book) in sorted(scripture.keys()):
        entries = sorted(scripture[(canon_idx, book)])
        out.append(f"## {book}")
        out.append("")
        # group by verse_key
        grouped: DefaultDict[str, Set[str]] = defaultdict(set)
        for _sort_key, vk, loc in entries:
            grouped[vk].add(loc)
        for vk in sorted(grouped, key=verse_key_sort):
            locs = sorted(grouped[vk], key=location_sort)
            out.append(f"- **{vk}** — {', '.join(locs)}")
        out.append("")

    out.append("")
    out.append("```{=openxml}")
    out.append('<w:br w:type="page"/>')
    out.append("```")
    out.append("")
    out.append("# Index II. Fathers, Councils, and Cited Authors")
    out.append("")
    out.append("*Alphabetical. Same L.C.S location scheme as Index I.*")
    out.append("")

    for name in sorted(fathers.keys(), key=str.lower):
        locs = sorted(fathers[name], key=location_sort)
        out.append(f"- **{name}** — {', '.join(locs)}")

    out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: build-indices.py <translation.md> [output.md]", file=sys.stderr)
        sys.exit(2)
    md_path = Path(sys.argv[1])
    result = build(md_path)
    if len(sys.argv) >= 3:
        Path(sys.argv[2]).write_text(result, encoding="utf-8", newline="\n")
        print(f"Wrote indices to {sys.argv[2]}")
    else:
        sys.stdout.write(result)
