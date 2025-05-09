#!/usr/bin/env python3

import re
import json
from pathlib import Path
from collections import OrderedDict

# Paths
GLOSSARY_MD_PATH = Path("docs/understanding-the-map/glossary.md")
GLOSSARY_JSON_PATH = Path("docs/assets/glossary.json")

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
    text = re.sub(r'$begin:math:display$([^$end:math:display$]+)\]$begin:math:text$[^)]+$end:math:text$', r'\1', text)  # strip [text](link)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def generate_tooltip_glossary(md_path):
    text = md_path.read_text()

    # Strip frontmatter and main title
    text = re.sub(r"(?s)^---.*?---", "", text).strip()
    text = re.sub(r"^# .*?\n", "", text)

    # Parse sections
    entries = re.split(r"\n##\s+", text)
    tooltip_dict = OrderedDict()

    for entry in entries:
        if not entry.strip():
            continue
        lines = entry.strip().split('\n', 1)
        if len(lines) < 2:
            continue
        term, body = lines
        slug = slugify(term)
        summary_raw = extract_summary(body)
        summary_clean = clean_summary(summary_raw)
        tooltip_dict[slug] = summary_clean

    return tooltip_dict

def main():
    if not GLOSSARY_MD_PATH.exists():
        print(f"❌ Could not find: {GLOSSARY_MD_PATH}")
        return

    tooltip_data = generate_tooltip_glossary(GLOSSARY_MD_PATH)
    GLOSSARY_JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    GLOSSARY_JSON_PATH.write_text(json.dumps(tooltip_data, indent=2))
    print(f"✅ Generated {GLOSSARY_JSON_PATH} with {len(tooltip_data)} entries.")

if __name__ == "__main__":
    main()