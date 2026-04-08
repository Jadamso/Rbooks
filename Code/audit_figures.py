"""Audit R figure code in book/*.qmd for style guide violations.

Usage:
    python3 Code/audit_figures.py           # all chapters
    python3 Code/audit_figures.py 01_05     # one chapter

Checks active (non-eval=F, non-commented) hist/plot/title calls for:
  - hist() missing border=NA or freq=F
  - Numeric color codes (col=2) or named colors (col='red')
  - Inline main='Title' instead of main=NA + title()
  - title() missing font.main=1
"""

import re
import glob
import sys


def get_full_call(lines, start_idx):
    """Gather lines from start_idx until parentheses balance."""
    depth = 0
    call = ''
    for i in range(start_idx, min(start_idx + 15, len(lines))):
        call += lines[i]
        depth += lines[i].count('(') - lines[i].count(')')
        if depth <= 0:
            break
    return call


def audit_file(filepath):
    with open(filepath) as fh:
        lines = fh.readlines()

    findings = []
    in_chunk = False
    eval_f = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        if stripped.startswith('```{r'):
            in_chunk = True
            eval_f = 'eval=F' in line or 'eval=FALSE' in line
            continue
        if stripped == '```':
            in_chunk = False
            eval_f = False
            continue
        if not in_chunk or eval_f or stripped.startswith('#'):
            continue

        call = get_full_call(lines, i)

        # --- hist() checks ---
        if re.search(r'\bhist\(', line) and 'plot=F' not in call and 'plot=FALSE' not in call:
            if 'border=NA' not in call and 'border = NA' not in call:
                findings.append((i + 1, 'hist() missing border=NA'))
            if not re.search(r'freq\s*=\s*(F|FALSE)', call) and 'probability=TRUE' not in call:
                findings.append((i + 1, 'hist() missing freq=F'))

        # --- Numeric or named color codes ---
        if re.search(r'\bcol\s*=\s*[2-9]\b', line):
            findings.append((i + 1, f'numeric color: {stripped[:80]}'))
        if re.search(r"\bcol\s*=\s*['\"](?:red|blue|green|orange|purple|yellow)['\"]", line):
            findings.append((i + 1, f'named color: {stripped[:80]}'))
        if re.search(r'\bcol\s*=\s*c\(\s*[0-9]', line):
            findings.append((i + 1, f'numeric color vector: {stripped[:80]}'))
        if re.search(r'\bcol\s*=\s*1:', line):
            findings.append((i + 1, f'color range: {stripped[:80]}'))

        # --- Inline main='Title' (non-empty, not NA) ---
        if re.search(r"\bmain\s*=\s*['\"][^'\"]+['\"]", line):
            # Exclude main=NA and main=''
            if not re.search(r"\bmain\s*=\s*['\"]['\"]", line):
                findings.append((i + 1, f'inline main=: {stripped[:80]}'))

        # --- title() missing font.main=1 ---
        if re.search(r'^\s*title\(', line):
            if 'font.main=1' not in call and 'font.main = 1' not in call:
                findings.append((i + 1, f'title() missing font.main=1'))

    return findings


if __name__ == '__main__':
    pattern = sys.argv[1] if len(sys.argv) > 1 else None

    files = sorted(glob.glob('book/[0-3]*.qmd'))
    if pattern:
        files = [f for f in files if pattern in f]

    total = 0
    for f in files:
        findings = audit_file(f)
        if findings:
            for lineno, msg in findings:
                print(f'{f}:{lineno}: {msg}')
            total += len(findings)

    if total == 0:
        print('No violations found.')
    else:
        print(f'\n{total} violation(s) found.')
