#!/usr/bin/env python3

import json
import re
from collections import OrderedDict
from pathlib import Path

GLOSSARY_MD_CANDIDATES = (
    Path("docs/understanding-the-map/appendices/glossary.md"),
    Path("docs/understanding-the-map/glossary.md"),
)
GLOSSARY_JSON_PATH = Path("docs/assets/glossary.json")
ENTRY_PATTERN = re.compile(r"^##\s+(.+?)\n(.*?)(?=^##\s+|\Z)", re.MULTILINE | re.DOTALL)

def slugify(term):
    # Use explicit anchor if present
    match = re.search(r"{#([^}]+)}", term)
    if match:
        return match.group(1)

    # Otherwise fallback to auto-slugify
    term_clean = re.sub(r"{#.*}$", "", term).strip()
    return re.sub(r"[^\w]+", "-", term_clean.lower()).strip("-")

def extract_summary(entry_body):
    # Priority 1: full block between <!-- summary:start --> and <!-- summary:end -->
    block_match = re.search(r'<!--\s*summary:start\s*-->(.*?)<!--\s*summary:end\s*-->', entry_body, re.DOTALL)
    if block_match:
        return block_match.group(1).strip()

    # Priority 2: single paragraph after <!-- summary -->
    marker_match = re.search(r'<!--\s*summary\s*-->\s*(.*?)(?:\n\n|\Z)', entry_body, re.DOTALL)
    if marker_match:
        return marker_match.group(1).strip()

    # Priority 3: fallback to first paragraph or text block
    return entry_body.strip().split('\n\n')[0].split('\n-')[0].strip()

def clean_summary(text):
    text = (
        text.replace('\n', ' ')
            .replace('\r', '')
            .replace('**', '')
            .replace('*', '')
            .replace('`', '')
            .replace('>', '')
            .replace('–', '-')
            .replace('—', '-')
    )
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def find_glossary_md_path():
    for path in GLOSSARY_MD_CANDIDATES:
        if path.exists():
            return path
    return None

def generate_tooltip_glossary(md_path):
    text = md_path.read_text(encoding="utf-8")

    # Strip frontmatter and main title
    text = re.sub(r"(?s)^---.*?---", "", text).strip()
    text = re.sub(r"^# .*?\n", "", text)

    tooltip_dict = OrderedDict()

    for match in ENTRY_PATTERN.finditer(text):
        term, body = match.groups()
        slug = slugify(term)
        summary_raw = extract_summary(body)
        summary_clean = clean_summary(summary_raw)
        tooltip_dict[slug] = summary_clean

    return tooltip_dict

def main():
    glossary_md_path = find_glossary_md_path()
    if glossary_md_path is None:
        searched = ", ".join(str(path) for path in GLOSSARY_MD_CANDIDATES)
        print(f"❌ Could not find a glossary source. Checked: {searched}")
        return

    tooltip_data = generate_tooltip_glossary(glossary_md_path)
    GLOSSARY_JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    GLOSSARY_JSON_PATH.write_text(json.dumps(tooltip_data, indent=2), encoding="utf-8")
    print(f"✅ Generated {GLOSSARY_JSON_PATH} from {glossary_md_path} with {len(tooltip_data)} entries.")

if __name__ == "__main__":
    main()
