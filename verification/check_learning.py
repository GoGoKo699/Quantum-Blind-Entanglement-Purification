#!/usr/bin/env python3
"""Check the shared learning map and local Markdown navigation."""
from pathlib import Path
import re
import unicodedata
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise SystemExit(message)


text = (ROOT / "learning/MILESTONES.md").read_text()
records = re.split(r"(?m)^### (M\d{2}) — (.+)$", text)
require(len(records) == 91, "Expected exactly 30 milestone records")
fields = ("Phase", "Central question", "Understanding target",
          "Dependencies and story role", "Conceptual connection", "Source pointers")
phase_counts = {}
for index in range(30):
    milestone, title, body = records[1 + 3 * index:4 + 3 * index]
    require(milestone == f"M{index + 1:02d}", f"Out-of-order milestone {milestone}")
    for field in fields:
        hits = re.findall(r"(?m)^- \*\*" + re.escape(field) + r":\*\* (.+)$", body)
        require(len(hits) == 1 and hits[0].strip(), f"{milestone}: missing/duplicate {field}")
    phase = re.search(r"(?m)^- \*\*Phase:\*\* (.+)$", body).group(1)
    expected = "Background/preliminaries." if index < 12 else "Narrative/innovation."
    require(phase == expected, f"{milestone}: inconsistent phase")
    phase_counts[phase] = phase_counts.get(phase, 0) + 1
    dependencies = re.search(r"(?m)^- \*\*Dependencies and story role:\*\* (.+)$", body).group(1)
    require(all(int(x) < index + 1 for x in re.findall(r"M(\d{2})", dependencies)),
            f"{milestone}: non-prior dependency")


def headings(source):
    result, repeats = set(), {}
    for heading in re.findall(r"(?m)^#{1,6} (.+)$", source):
        heading = heading.lower().strip().replace("`", "")
        slug = "".join(c for c in heading if c in " -_" or unicodedata.category(c)[0] in "LN")
        slug = slug.replace(" ", "-")
        count = repeats.get(slug, 0)
        repeats[slug] = count + 1
        result.add(slug + (f"-{count}" if count else ""))
    return result


links = pages = 0
for page in sorted(ROOT.rglob("*.md")):
    if ".git" in page.parts:
        continue
    pages += 1
    source = page.read_text()
    # Repository reader pages use ordinary inline Markdown links.
    for raw in re.findall(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)", source):
        target = raw.strip().strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            continue
        path = (page.parent / unquote(parsed.path)).resolve() if parsed.path else page
        require(path.is_relative_to(ROOT), f"{page.relative_to(ROOT)}: escaping link {raw}")
        require(path.exists(), f"{page.relative_to(ROOT)}: missing link {raw}")
        if parsed.fragment and path.is_file() and path.suffix == ".md":
            require(unquote(parsed.fragment) in headings(path.read_text()),
                    f"{page.relative_to(ROOT)}: missing heading {raw}")
        links += 1

for name in ("README.md", "llms.txt"):
    entry = (ROOT / name).read_text()
    require("learning/MILESTONES.md" in entry and "learning/ANCHOR.md" in entry,
            f"{name}: missing direct learning routes")
require("2010" in (ROOT / "learning/ANCHOR.md").read_text(), "Missing anchor edition")
print(f"PASS: M01–M30, 12 background/18 innovation, six fields each, prior dependencies; {links} local links in {pages} Markdown pages.")
print("Scope: structure and navigation; conceptual accuracy requires the separate reading review.")
