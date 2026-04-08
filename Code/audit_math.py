#!/usr/bin/env python3
"""Check inline math for spaces inside dollar-sign delimiters.

Spaces after the opening $ or before the closing $ cause Quarto/Pandoc
to render the expression as literal text instead of math.

Usage:
    python3 Code/audit_math.py            # all chapters
    python3 Code/audit_math.py 01_09      # chapters matching '01_09'
"""

import glob
import sys


def audit_file(filepath):
    """Return list of (line_number, issues, line_text, math_text) tuples."""
    with open(filepath) as fh:
        lines = fh.readlines()

    results = []
    in_code = False
    in_yaml = False
    yaml_count = 0

    for i, line in enumerate(lines, 1):
        stripped = line.strip()

        # track YAML frontmatter
        if i <= 5 and stripped == '---':
            yaml_count += 1
            if yaml_count == 1:
                in_yaml = True
                continue
            else:
                in_yaml = False
                continue
        if in_yaml:
            continue

        # track fenced code blocks
        if stripped.startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            continue

        # skip display math lines
        if stripped.startswith('$$'):
            continue

        # parse inline math
        text = line
        pos = 0
        while pos < len(text):
            idx = text.find('$', pos)
            if idx == -1:
                break
            # skip escaped \$
            if idx > 0 and text[idx - 1] == '\\':
                pos = idx + 1
                continue
            # skip $$
            if idx + 1 < len(text) and text[idx + 1] == '$':
                pos = idx + 2
                close_dd = text.find('$$', pos)
                if close_dd != -1:
                    pos = close_dd + 2
                continue

            # find matching closing $
            close = idx + 1
            found_close = False
            while close < len(text):
                c = text.find('$', close)
                if c == -1:
                    break
                if c > 0 and text[c - 1] == '\\':
                    close = c + 1
                    continue
                if c + 1 < len(text) and text[c + 1] == '$':
                    close = c + 2
                    continue
                close = c
                found_close = True
                break

            if not found_close:
                pos = idx + 1
                continue

            math = text[idx + 1:close]
            if not math:
                pos = close + 1
                continue

            issues = []
            if math[0] == ' ':
                issues.append('space after opening $')
            if math[-1] == ' ':
                issues.append('space before closing $')

            if issues:
                results.append((i, ' & '.join(issues), line.rstrip(), math))

            pos = close + 1

    return results


def main():
    filter_str = sys.argv[1] if len(sys.argv) > 1 else None
    files = sorted(glob.glob('book/*.qmd'))
    if filter_str:
        files = [f for f in files if filter_str in f]

    total = 0
    for f in files:
        hits = audit_file(f)
        if hits:
            fname = f.split('/')[-1]
            for lineno, issues, line_text, math_text in hits:
                snip = line_text
                if len(snip) > 120:
                    snip = snip[:117] + '...'
                print(f'{fname}:{lineno}: {issues}')
                print(f'  {snip}')
                print(f'  Math: ${math_text}$')
                print()
            total += len(hits)

    if total == 0:
        print('No inline math spacing issues found.')
    else:
        print(f'{total} issue(s) found.')


if __name__ == '__main__':
    main()
