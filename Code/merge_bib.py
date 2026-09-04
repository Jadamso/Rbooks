#!/usr/bin/env python3
"""Merge external BibTeX files into book/references.bib.

Quarto only renders entries that are actually cited, so pulling in the full
teaching bibliographies costs nothing at render time and lets new citations be
added to the text without hunting for the reference again.

Entries already in book/references.bib always win, so hand-edits made here are
never overwritten by a later merge. Among the source files, earlier arguments
win over later ones. Keys are compared case-insensitively, because the same
work appears as both `racine2012` and `Racine2012` across the source files.

Usage:
    python3 Code/merge_bib.py                    # merge the default sources
    python3 Code/merge_bib.py path/to/other.bib  # merge specific files
"""

import os
import re
import sys

HDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET = os.path.join(HDIR, 'book', 'references.bib')

DEFAULT_SOURCES = [
    os.path.expanduser('~/Desktop/Teaching/Microeconometrics/Bibliography.bib'),
    os.path.expanduser('~/Desktop/Teaching/SpatialEconometrics/Bibliography.bib'),
]

# An entry starts at @type{key, and runs until its braces balance.
ENTRY_START = re.compile(r'@(\w+)\s*\{\s*([^,\s]+)\s*,', re.MULTILINE)


def parse_entries(text):
    """Return [(entry_type, key, raw_text)] for every entry in a .bib string."""
    entries = []
    for match in ENTRY_START.finditer(text):
        entry_type, key = match.group(1), match.group(2)
        # @string/@preamble/@comment are not references; skip them.
        if entry_type.lower() in ('string', 'preamble', 'comment'):
            continue
        # Walk forward from the opening brace until the braces balance.
        start = text.index('{', match.start())
        depth, i = 0, start
        while i < len(text):
            if text[i] == '{':
                depth += 1
            elif text[i] == '}':
                depth -= 1
                if depth == 0:
                    break
            i += 1
        if depth != 0:  # unbalanced entry at end of file
            continue
        entries.append((entry_type, key, text[match.start():i + 1]))
    return entries


def read(path):
    with open(path, encoding='utf-8', errors='replace') as handle:
        return handle.read()


def main():
    sources = sys.argv[1:] or DEFAULT_SOURCES

    merged = {}      # lowercased key -> raw entry text
    order = []       # lowercased keys, in insertion order
    provenance = {}  # lowercased key -> file it came from
    skipped = []     # (key, file) pairs dropped as duplicates

    # Existing entries win, so anything hand-edited in the book survives a merge.
    files = [TARGET] + [s for s in sources if os.path.exists(s)]
    for path in files:
        if not os.path.exists(path):
            print('  missing, skipped: {}'.format(path))
            continue
        entries = parse_entries(read(path))
        added = 0
        for _entry_type, key, raw in entries:
            lower = key.lower()
            if lower in merged:
                skipped.append((key, os.path.basename(path)))
                continue
            merged[lower] = raw
            order.append(lower)
            provenance[lower] = os.path.basename(path)
            added += 1
        print('  {:>4} entries ({} new) from {}'.format(
            len(entries), added, os.path.basename(path)))

    order.sort()
    body = '\n\n'.join(merged[k] for k in order)
    with open(TARGET, 'w', encoding='utf-8') as handle:
        handle.write(body + '\n')

    print('\nWrote {} unique entries to {}'.format(len(order), TARGET))
    if skipped:
        print('Dropped {} duplicate keys (first file wins):'.format(len(skipped)))
        for key, src in skipped[:20]:
            print('  {} (from {})'.format(key, src))
        if len(skipped) > 20:
            print('  ... and {} more'.format(len(skipped) - 20))


if __name__ == '__main__':
    main()
