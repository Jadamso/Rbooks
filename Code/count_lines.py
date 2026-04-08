#!/usr/bin/env python3
"""Compute Math / Code / Text line breakdown and word count for each .qmd chapter.

Usage:
    python3 count_lines.py          # all chapters
    python3 count_lines.py 01_09    # single chapter (substring match)

Prints a Markdown table matching the format in ToDo.md,
followed by outlier reports (short and long chapters by word count).
"""

import glob, os, re, sys, statistics


def classify(filepath):
    with open(filepath) as f:
        content = f.read()

    lines = content.splitlines()
    total = len(lines)
    words = len(content.split())
    in_code = False
    in_math = False
    code = 0
    math = 0
    text = 0
    sections = 0
    subsections = 0

    for line in lines:
        s = line.strip()
        # Code fences
        if s.startswith('```'):
            in_code = not in_code
            code += 1
            continue
        if in_code:
            code += 1
            continue
        # Math block delimiters
        if re.match(r'\\begin\{(eqnarray|align|equation)', s):
            in_math = True
            math += 1
            continue
        if re.match(r'\\end\{(eqnarray|align|equation)', s):
            in_math = False
            math += 1
            continue
        if in_math:
            math += 1
            continue
        # Display math ($$)
        if s.startswith('$$'):
            math += 1
            continue
        # Count sections and subsections (outside code blocks)
        if re.match(r'^## ', line):
            sections += 1
        elif re.match(r'^#### ', line):
            subsections += 1
        # Everything else
        text += 1

    return total, math, code, text, words, sections, subsections


def label_from_filename(fname):
    """Turn '01_09_AdvancedProbability.qmd' into '01_09 Advanced Probability'."""
    stem = os.path.splitext(fname)[0]
    parts = stem.split('_', 2)
    prefix = parts[0] + '_' + parts[1]
    title = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', parts[2]) if len(parts) > 2 else ''
    return f'{prefix} {title}'


def part_header(prefix):
    headers = {
        '00': '**Part 0 — Getting Started**',
        '01': '**Part 1 — Univariate Data**',
        '02': '**Part 2 — Bivariate Data**',
        '03': '**Part 3 — Multivariate Data**',
        '04': '**Appendices (Unused)**',
    }
    return headers.get(prefix)


def is_stub(total):
    return total <= 10


if __name__ == '__main__':
    bookdir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'book')
    files = sorted(glob.glob(os.path.join(bookdir, '[0-9][0-9]_[0-9][0-9]_*.qmd')))

    # Optional filter
    filt = sys.argv[1] if len(sys.argv) > 1 else None
    if filt:
        files = [f for f in files if filt in os.path.basename(f)]

    # Collect results
    results = []
    for fp in files:
        fname = os.path.basename(fp)
        total, math, code, text, words, sections, subsections = classify(fp)
        lbl = label_from_filename(fname)
        part = fname[:2]
        results.append((fp, fname, part, lbl, total, math, code, text, words,
                         sections, subsections))

    # Print table
    print('| Chapter | Words | Lines | Math | Code | Text |')
    print('|---|---:|---:|---:|---:|---:|')

    prev_part = None
    for fp, fname, part, lbl, total, math, code, text, words, sections, subsections in results:
        if part != prev_part and not filt:
            hdr = part_header(part)
            if hdr:
                print(f'| {hdr} |')
            prev_part = part

        def pct(n):
            return f'{n} ({round(100*n/total)}%)' if total else '0 (0%)'

        print(f'| {lbl} | {words} | {total} | {pct(math)} | {pct(code)} | {pct(text)} |')

    # Structure table: sections and subsections per chapter
    print('\n#### Chapter Structure (sections `##` and subsections `####`)\n')
    print('| Chapter | Sections | Subsections |')
    print('|---|---:|---:|')

    prev_part = None
    for fp, fname, part, lbl, total, math, code, text, words, sections, subsections in results:
        if part != prev_part and not filt:
            hdr = part_header(part)
            if hdr:
                print(f'| {hdr} |')
            prev_part = part
        print(f'| {lbl} | {sections} | {subsections} |')

    # Outlier analysis (skip stubs and appendices, only when showing all chapters)
    if not filt:
        chapters = [(lbl, total, words, sections, subsections)
                     for fp, fname, part, lbl, total, math, code, text, words,
                     sections, subsections in results
                     if not is_stub(total) and part not in ('04',)]

        if len(chapters) >= 5:
            # Word count outliers
            word_counts = [w for _, _, w, _, _ in chapters]
            med = statistics.median(word_counts)
            q1 = statistics.median([w for w in word_counts if w <= med])
            q3 = statistics.median([w for w in word_counts if w >= med])
            iqr = q3 - q1
            lo = q1 - 1.5 * iqr
            hi = q3 + 1.5 * iqr

            short = [(lbl, lines, words)
                     for lbl, lines, words, _, _ in chapters if words < lo]
            long_ = [(lbl, lines, words)
                     for lbl, lines, words, _, _ in chapters if words > hi]

            print(f'\n**Word-count outliers** (median {med} words, IQR [{round(q1)}–{round(q3)}], '
                  f'fence [{round(lo)}–{round(hi)}])')

            if short:
                short.sort(key=lambda r: r[2])
                print('\nShort:')
                for lbl, lines, words in short:
                    print(f'- {lbl}: {words} words ({lines} lines)')
            else:
                print('\nShort: none')

            if long_:
                long_.sort(key=lambda r: -r[2])
                print('\nLong:')
                for lbl, lines, words in long_:
                    print(f'- {lbl}: {words} words ({lines} lines)')
            else:
                print('\nLong: none')

            # Structure outliers
            def iqr_outliers(values, labels):
                med = statistics.median(values)
                q1 = statistics.median([v for v in values if v <= med])
                q3 = statistics.median([v for v in values if v >= med])
                iqr = q3 - q1
                lo = q1 - 1.5 * iqr
                hi = q3 + 1.5 * iqr
                low = [(lbl, v) for lbl, v in zip(labels, values) if v < lo]
                high = [(lbl, v) for lbl, v in zip(labels, values) if v > hi]
                return med, lo, hi, low, high

            labels = [lbl for lbl, _, _, _, _ in chapters]
            sec_vals = [s for _, _, _, s, _ in chapters]
            sub_vals = [s for _, _, _, _, s in chapters]

            print('\n**Structure outliers**')
            for metric, vals in [('Sections', sec_vals), ('Subsections', sub_vals)]:
                med, lo, hi, low, high = iqr_outliers(vals, labels)
                items = []
                for lbl, v in low:
                    items.append(f'{lbl} ({v}, low)')
                for lbl, v in high:
                    items.append(f'{lbl} ({v}, high)')
                if items:
                    print(f'\n{metric} (median {med}, fence [{lo:.0f}–{hi:.0f}]):')
                    for item in items:
                        print(f'- {item}')
                else:
                    print(f'\n{metric} (median {med}): no outliers')
