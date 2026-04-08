#!/usr/bin/env python3
"""Fix R code style in .qmd files:
1. Spaces around ~ in formulas (not in expression() calls)
2. Spaces after commas
3. Double quotes -> single quotes
Only modifies content inside R code chunks.
"""

import re
import sys
from pathlib import Path

def is_in_expression(line, pos):
    """Check if position is inside an expression() call."""
    # Look backwards from pos for 'expression('
    before = line[:pos]
    # Find the last 'expression(' before this position
    idx = before.rfind('expression(')
    if idx == -1:
        return False
    # Count parens from that point to see if we're still inside
    depth = 0
    for i in range(idx, pos):
        if line[i] == '(':
            depth += 1
        elif line[i] == ')':
            depth -= 1
    return depth > 0

def fix_tilde(line):
    """Add spaces around ~ in formula contexts."""
    result = []
    i = 0
    while i < len(line):
        if line[i] == '~' and not is_in_expression(line, i):
            # Check if spaces are missing
            before = result[-1] if result else ' '
            after = line[i+1] if i+1 < len(line) else ' '
            if before != ' ' and before != '\t':
                result.append(' ')
            result.append('~')
            if after != ' ' and after != '\n' and after != '\t':
                result.append(' ')
            i += 1
        else:
            result.append(line[i])
            i += 1
    return ''.join(result)

def fix_commas(line):
    """Add space after commas that aren't followed by a space."""
    result = []
    i = 0
    while i < len(line):
        result.append(line[i])
        if line[i] == ',' and i + 1 < len(line) and line[i+1] not in (' ', '\n', '\r'):
            result.append(' ')
        i += 1
    return ''.join(result)

def fix_quotes(line):
    """Replace double quotes with single quotes in R code."""
    result = []
    i = 0
    while i < len(line):
        if line[i] == '"':
            # Find matching close quote
            j = line.index('"', i + 1) if '"' in line[i+1:] else -1
            if j == -1:
                result.append(line[i])
                i += 1
            else:
                inner = line[i+1:j]
                # Don't change if inner contains single quotes
                if "'" in inner:
                    result.append(line[i:j+1])
                else:
                    result.append("'" + inner + "'")
                i = j + 1
        else:
            result.append(line[i])
            i += 1
    return ''.join(result)

def process_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    in_chunk = False
    changed = 0
    new_lines = []

    for line in lines:
        orig = line

        # Track R code chunks
        if re.match(r'^```\{r', line):
            in_chunk = True
            new_lines.append(line)
            continue
        if line.startswith('```') and in_chunk:
            in_chunk = False
            new_lines.append(line)
            continue

        if in_chunk:
            # Skip comment-only lines that are prose (# long sentence...)
            stripped = line.lstrip()
            line = fix_commas(line)
            line = fix_tilde(line)
            line = fix_quotes(line)

        if line != orig:
            changed += 1
        new_lines.append(line)

    if changed > 0:
        with open(filepath, 'w') as f:
            f.writelines(new_lines)
        print(f"  {filepath.name}: {changed} lines changed")
    else:
        print(f"  {filepath.name}: no changes")
    return changed

def main():
    book_dir = Path('/home/jadamson/Desktop/Packages/Rbooks/book')
    qmd_files = sorted(book_dir.glob('[0-3]*.qmd'))

    total = 0
    for f in qmd_files:
        total += process_file(f)
    print(f"\nTotal: {total} lines changed across {len(qmd_files)} files")

if __name__ == '__main__':
    main()
