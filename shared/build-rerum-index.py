"""Build a Rerum (subject) index for a Scholastic Lutherans translation MD.

Approach:

  1. Walk the MD tracking (Liber, Cap, Casus) Roman-numeral context per line.
  2. From each Chapter and Casus title, extract topic keywords: content
     nouns after stripping stopwords, function words, and interrogatives.
  3. Apply a curated synonyms table so morphological variants and near-syns
     collapse to a canonical head (e.g. "marriages" -> "marriage",
     "adulterous" -> "adultery").
  4. For each canonical head, walk the whole body body-text scanning for
     the head *or any of its variants* as whole words. Record L.C.S loc.
  5. Emit alphabetical Rerum index in Markdown.

Location scheme matches Index I/II: L.C.S (Liber.Chapter.Casus).

Usage:  python build-rerum-index.py <path/to/translation.md> [output.md]
"""

from __future__ import annotations
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import DefaultDict, Dict, List, Set, Tuple

LIBER_RE = re.compile(r"^#\s+Liber\s+([IVXL]+)\b", re.IGNORECASE)
CHAPTER_RE = re.compile(r"^##\s+Chapter\s+([IVXL]+)\.?\s+(.+?)\s*$", re.IGNORECASE)
CASUS_RE = re.compile(r"^###\s+Casus\s+([IVXL]+)\.?\s+(.+?)\s*$", re.IGNORECASE)

# Curated Rerum: canonical topic head -> list of surface variants
# (all lowercase). Head-form is what appears in the index.
# Reasonably comprehensive for Balduin's Casibus Conscientiae.
TOPICS: Dict[str, List[str]] = {
    # 1. God + religion (Liber II mainly)
    "angels": ["angel", "angels", "angelic"],
    "adiaphora": ["adiaphora", "adiaphoron", "indifferent things"],
    "adoption": ["adoption"],
    "adultery": ["adultery", "adulterer", "adulteress", "adulterous", "adulteries"],
    "agony": ["agony", "agonies"],
    "alms": ["alms", "almsgiving", "almsdeeds", "elee mosynae"],
    "anabaptists": ["anabaptist", "anabaptists"],
    "anathema": ["anathema", "anathematize", "anathemas"],
    "angels": ["angel", "angels", "angelic"],
    "anger": ["anger", "wrath", "wrathful", "iracundia"],
    "apostasy": ["apostasy", "apostate", "apostates"],
    "arius": ["arius", "arian", "arianism"],
    "astrology": ["astrology", "astrologer", "astrologers"],
    "atheism": ["atheism", "atheist", "atheists"],
    "authority (paternal)": ["paternal authority", "paternal power"],
    "auricular confession": ["auricular confession", "private confession"],
    "baptism": ["baptism", "baptize", "baptized", "baptizes", "baptizing"],
    "bellarmine": ["bellarmine"],
    "bishops": ["bishop", "bishops", "episcopal", "episcopate"],
    "blasphemy": ["blasphemy", "blaspheme", "blasphemer", "blasphemies", "blaspheming"],
    "blessing": ["blessing", "blessings"],
    "body of Christ": ["body of christ"],
    "brothels": ["brothel", "brothels", "lupanar", "lupanaria"],
    "brotherhood": ["brother", "brothers", "sister", "sisters", "fraternal"],
    "burial": ["burial", "sepulchre", "sepulchres", "sepulture"],
    "calvinists": ["calvinist", "calvinists", "calvin"],
    "case of conscience": ["case of conscience", "cases of conscience"],
    "casuistry": ["casuistry"],
    "catechism": ["catechism", "catechesis", "catechetical"],
    "celibacy": ["celibacy", "celibate", "celibates"],
    "ceremonies": ["ceremony", "ceremonies", "ceremonial"],
    "charity": ["charity", "charitable"],
    "children": ["child", "children", "childhood"],
    "church": ["church", "churches", "ecclesiastical"],
    "circumcision": ["circumcision", "circumcise", "circumcised"],
    "clergy": ["clergy", "clerical", "clerics", "cleric"],
    "commandments": ["commandment", "commandments", "decalogue"],
    "communion": ["communion", "communicant", "communicants"],
    "concord": ["concord", "concordia"],
    "confession": ["confession", "confessions"],
    "confirmation": ["confirmation"],
    "conjugal debt": ["conjugal debt", "conjugal right"],
    "conscience": ["conscience", "consciences"],
    "consent (parental)": ["parental consent"],
    "consolation": ["consolation", "console", "consoled"],
    "contempt": ["contempt", "contemn", "contemner", "contemners"],
    "correction (fraternal)": ["fraternal correction", "brotherly correction"],
    "councils": ["council of trent", "council of nicaea", "nicene council", "chalcedon", "constantinople"],
    "creation": ["creation", "creator", "created"],
    "creed": ["creed", "creeds"],
    "cross": ["cross"],
    "damnation": ["damnation", "damned"],
    "death": ["death", "die", "dying", "dead"],
    "decalogue": ["decalogue"],
    "demons": ["demon", "demons", "demonic"],
    "desertion": ["desertion", "deserter", "deserters"],
    "devil": ["devil", "devils", "satan"],
    "discipline": ["discipline", "disciplinary"],
    "dispensation": ["dispensation", "dispensations", "dispense"],
    "divination": ["divination", "diviner", "diviners"],
    "divorce": ["divorce", "divorces"],
    "doctrine": ["doctrine", "doctrines", "doctrinal"],
    "domestics": ["domestic", "domestics", "domestic servants"],
    "doubt": ["doubt", "doubtful", "doubting"],
    "drunkenness": ["drunkenness", "drunkard", "drunkards", "intoxication"],
    "duty": ["duty", "duties", "office", "offices"],
    "education": ["education", "educate", "educating"],
    "election": ["election", "elect", "elected"],
    "elders": ["elder", "elders"],
    "enemies": ["enemy", "enemies"],
    "envy": ["envy", "envier", "envious"],
    "eternal life": ["eternal life"],
    "eucharist": ["eucharist"],
    "excommunication": ["excommunication", "excommunicate", "excommunicated"],
    "faith": ["faith", "faithful", "faithfully", "faithless"],
    "family": ["family", "families", "familial"],
    "fasting": ["fast", "fasting", "fasts", "abstinence"],
    "fathers (church)": ["church father", "church fathers", "fathers of the church"],
    "fear of god": ["fear of god"],
    "feasts": ["feast", "feasts", "festival", "festivals", "holy days"],
    "fornication": ["fornication", "fornicator", "fornicators"],
    "friendship": ["friendship", "friend", "friends"],
    "gifts": ["gift", "gifts", "gift-giving"],
    "god": ["god", "godhead"],
    "goods": ["goods"],
    "gospel": ["gospel", "gospels"],
    "grace": ["grace", "graces", "gracious"],
    "gratitude": ["gratitude", "grateful", "ingratitude"],
    "hearing the word": ["hearing the divine word", "hearing the word"],
    "heart": ["heart", "hearts"],
    "heresy": ["heresy", "heretic", "heretical", "heresies"],
    "holy communion": ["holy communion", "lord's supper", "supper of the lord", "eucharist"],
    "holy spirit": ["holy spirit", "holy ghost"],
    "homicide": ["homicide", "murder", "murders", "murderer"],
    "honor": ["honor", "honour", "honors", "honored", "honoured"],
    "hospitality": ["hospitality"],
    "hunt / hunting": ["hunt", "hunting", "hunter", "hunters", "venatio"],
    "humaneness": ["humaneness", "humanitas", "humanity"],
    "hypocrisy": ["hypocrisy", "hypocrite", "hypocrites"],
    "idolatry": ["idolatry", "idols", "idol", "idolater", "idolaters"],
    "image of god": ["image of god", "imago dei"],
    "imprecation": ["imprecation", "imprecations", "curse", "cursing"],
    "impotence": ["impotence", "impotent"],
    "incest": ["incest", "incestuous"],
    "infants": ["infant", "infants", "little-ones"],
    "infidels": ["infidel", "infidels", "unbeliever", "unbelievers"],
    "inheritance": ["inheritance", "heir", "heirs", "disinherit", "disinherited"],
    "innocent": ["innocent", "innocence", "innocents"],
    "intention": ["intention", "intentions"],
    "invocation": ["invocation", "invoke", "invoking"],
    "jesuits": ["jesuit", "jesuits"],
    "jews": ["jew", "jews", "jewish"],
    "judgment": ["judgment", "judge", "judges", "judging"],
    "just war": ["just war", "just wars"],
    "justice": ["justice", "just", "justness"],
    "justification": ["justification"],
    "keys of the church": ["keys of the church", "key of david", "power of the keys"],
    "kingdom of god": ["kingdom of god"],
    "kinsmen": ["kinsmen", "kindred", "propinqui", "cognati"],
    "labor": ["labor", "labour"],
    "laity": ["laity", "layman", "laymen"],
    "laws": ["law", "laws", "legal", "legislator"],
    "lending": ["lending", "loan", "loans", "usury", "usurer"],
    "lie": ["lie", "lies", "lying", "mendacity", "mendacium"],
    "lord's supper": ["lord's supper", "supper of the lord"],
    "love": ["love", "loves", "loving"],
    "lust": ["lust", "lusts", "lustful"],
    "magic": ["magic", "magician", "magicians", "magi"],
    "magistrate": ["magistrate", "magistrates", "magistracy"],
    "marriage": ["marriage", "marriages", "matrimony", "matrimonial", "conjugal", "conjugium"],
    "masters": ["master", "masters"],
    "meditation": ["meditation", "meditate"],
    "mercy": ["mercy", "mercies", "merciful"],
    "military": ["military", "soldier", "soldiers", "soldiering", "militia"],
    "ministers of word": ["minister of the word", "ministers of the word", "ministry of the word"],
    "ministry": ["ministry", "minister", "ministers", "ministering"],
    "miracles": ["miracle", "miracles", "miraculous"],
    "monastery": ["monastery", "monasteries", "monk", "monks", "monastic", "monasticism"],
    "morals": ["moral", "morals", "morality"],
    "obedience": ["obedience", "obey", "obeying", "disobedience", "disobey"],
    "oath": ["oath", "oaths", "swearing", "swore", "sworn", "perjury", "perjured"],
    "office of the magistrate": ["office of the magistrate", "office of magistrate"],
    "opinion": ["opinion", "opinions", "opinionative"],
    "ordination": ["ordination", "ordain", "ordained"],
    "papacy": ["papacy", "pope", "popes", "papist", "papists", "papal", "roman pontiff"],
    "parents": ["parent", "parents", "parental", "paternal", "maternal"],
    "penitence": ["penitence", "penitent", "repentance", "repent"],
    "peril of life": ["peril of life", "danger of life"],
    "persecution": ["persecution", "persecute", "persecuted", "persecutors"],
    "piety": ["piety", "pious", "piously"],
    "poverty": ["poverty", "poor", "beggar", "beggars", "paupers"],
    "prayer": ["prayer", "prayers", "praying"],
    "preacher / preaching": ["preacher", "preachers", "preaching", "sermon", "sermons"],
    "predestination": ["predestination", "predestined", "predestine"],
    "priest": ["priest", "priests", "priesthood", "sacerdotal", "sacerdotium"],
    "princes": ["prince", "princes", "princely"],
    "prisoners": ["prisoner", "prisoners", "captive", "captives"],
    "prohibited degrees": ["prohibited degree", "prohibited degrees", "degrees of consanguinity"],
    "prophets": ["prophet", "prophets", "prophecy", "prophesying"],
    "prostitutes": ["prostitute", "prostitutes", "harlot", "harlots", "prostitution"],
    "punishment": ["punishment", "punish", "punished", "penalty", "penalties"],
    "reason": ["reason", "reasons", "rational"],
    "reconciliation": ["reconciliation", "reconcile", "reconciled"],
    "regeneration": ["regeneration", "regenerate", "regenerated"],
    "religion": ["religion", "religious"],
    "reliquiae": ["relic", "relics"],
    "remarriage": ["second marriage", "second marriages", "iteratae nuptiae", "remarry", "remarriage"],
    "reprobate": ["reprobate", "reprobates", "reprobation"],
    "republic (respublica)": ["republic", "commonwealth", "respublica"],
    "resurrection": ["resurrection"],
    "revelation": ["revelation"],
    "rome": ["rome", "roman"],
    "sabbath": ["sabbath", "sabbaths", "sunday"],
    "sacrament": ["sacrament", "sacraments", "sacramental"],
    "sacrifice": ["sacrifice", "sacrifices", "sacrificial"],
    "salvation": ["salvation", "salvific", "saving"],
    "sanctification": ["sanctification", "sanctify", "sanctified"],
    "satan": ["satan"],
    "scandal": ["scandal", "scandalous", "scandalize", "scandals"],
    "schools": ["school", "schools", "schoolmaster"],
    "scripture": ["scripture", "scriptures", "scriptural", "sacred letters", "canonical scripture"],
    "scruple": ["scruple", "scrupulous", "scruples"],
    "seared conscience": ["seared conscience", "cauterized conscience"],
    "second table": ["second table"],
    "sedition": ["sedition", "seditious", "rebellion", "rebel", "rebellious"],
    "sermon": ["sermon", "sermons", "preaching"],
    "servants": ["servant", "servants", "servitude", "slave", "slaves"],
    "sin": ["sin", "sins", "sinful", "sinner", "sinners"],
    "singing": ["singing", "sing", "hymn", "hymns", "psalmody"],
    "slander": ["slander", "slanderer", "slandering", "calumny", "calumnies"],
    "sobriety": ["sobriety", "sober"],
    "sodomy": ["sodomy", "sodomite", "sodomites"],
    "soul": ["soul", "souls"],
    "specters": ["specter", "specters", "spectres", "phantoms", "ghost", "ghosts"],
    "spouses": ["spouse", "spouses"],
    "spurii": ["spurious", "spurius", "spurii", "bastard", "bastards", "illegitimate"],
    "state (of life)": ["state of life"],
    "stealing": ["theft", "thefts", "steal", "stealing", "thief", "thieves"],
    "study": ["study", "studies", "studious"],
    "subject": ["subject", "subjects", "subjection"],
    "suicide": ["suicide"],
    "sustenance": ["sustenance", "alimenta", "alimentation"],
    "swearing": ["swear", "swearing", "sworn", "oath", "oaths"],
    "tithes": ["tithe", "tithes", "decimae"],
    "toleration": ["toleration", "tolerate", "tolerated"],
    "tongue": ["tongue", "tongues"],
    "trent (council of)": ["trent", "council of trent", "trident"],
    "tribute": ["tribute", "tributes", "tax", "taxes"],
    "trinity": ["trinity", "trinitarian"],
    "truth": ["truth", "true", "truly"],
    "tyranny": ["tyranny", "tyrant", "tyrants", "tyrannical"],
    "unbelievers": ["unbeliever", "unbelievers", "infidel", "infidels"],
    "usury": ["usury", "usurer", "usurers", "usurious"],
    "vengeance": ["vengeance", "avenge"],
    "vice": ["vice", "vices", "vicious"],
    "virginity": ["virginity", "virgin", "virgins"],
    "virtue": ["virtue", "virtues", "virtuous"],
    "vocation": ["vocation", "vocations", "calling"],
    "vows": ["vow", "vows"],
    "war": ["war", "wars", "warfare"],
    "wealth": ["wealth", "wealthy", "riches", "rich"],
    "wife": ["wife", "wives"],
    "will (of God)": ["will of god"],
    "witness": ["witness", "witnesses"],
    "wittenberg": ["wittenberg"],
    "women": ["woman", "women"],
    "word (of God)": ["word of god", "divine word"],
    "world": ["world", "worlds", "worldly"],
    "worship": ["worship", "worshipping", "cult", "adoration"],
    "wounded conscience": ["wounded conscience", "wounded consciences"],
}


def build(md_path: Path) -> str:
    liber = chap = casus = None
    front_matter = True

    # Build a "content chunk per L.C.S location" mapping so we scan each
    # topic only once against each chunk.
    chunks: Dict[str, List[str]] = defaultdict(list)

    for line in md_path.read_text(encoding="utf-8").splitlines():
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

        loc_parts = [p for p in (liber, chap, casus) if p]
        if not loc_parts:
            continue
        loc = ".".join(loc_parts)
        chunks[loc].append(line.lower())

    # For each topic, scan every chunk for any variant as whole word
    index: Dict[str, Set[str]] = defaultdict(set)
    for topic, variants in TOPICS.items():
        patterns = [re.compile(r"(?<![A-Za-z])" + re.escape(v) + r"(?![A-Za-z])")
                    for v in variants]
        for loc, lines in chunks.items():
            body = " ".join(lines)
            if any(p.search(body) for p in patterns):
                index[topic].add(loc)

    return render(index)


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


def render(index: Dict[str, Set[str]]) -> str:
    out = []
    out.append("")
    out.append("```{=openxml}")
    out.append('<w:br w:type="page"/>')
    out.append("```")
    out.append("")
    out.append("# Index III. Subjects (Rerum)")
    out.append("")
    out.append("*Alphabetical topical index. Location scheme L.C.S "
               "(Liber.Chapter.Casus, all Roman). Entries collect every "
               "Casus in which the topic — or one of its variants — is "
               "discussed. Generated from a curated topic list; not "
               "exhaustive.*")
    out.append("")

    for topic in sorted(index.keys()):
        locs = sorted(index[topic], key=location_sort)
        if not locs:
            continue
        # Cap at ~40 locations per topic to keep index readable
        if len(locs) > 40:
            shown = locs[:40] + ["…"]
        else:
            shown = locs
        out.append(f"- **{topic}** — {', '.join(shown)}")

    out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: build-rerum-index.py <translation.md> [output.md]",
              file=sys.stderr)
        sys.exit(2)
    result = build(Path(sys.argv[1]))
    if len(sys.argv) >= 3:
        Path(sys.argv[2]).write_text(result, encoding="utf-8", newline="\n")
        print(f"Wrote Rerum index to {sys.argv[2]}")
    else:
        sys.stdout.write(result)
