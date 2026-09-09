#!/usr/bin/env python3
"""Identify which datasets are used in each .qmd chapter.

Usage:
    python3 list_datasets.py              # all chapters
    python3 list_datasets.py 01_09        # single chapter (substring match)
    python3 list_datasets.py --by-dataset # grouped by dataset instead of chapter

Scans R code blocks for data(), read.csv(), library(wooldridge/Ecdat),
and direct references to known built-in datasets.
"""

import glob, os, re, sys


# ── Known datasets ──────────────────────────────────────────────────────────
# Built-in R datasets referenced directly (without data() call)
BUILTIN_DATASETS = {
    'USArrests':     'datasets (built-in)',
    'UCBAdmissions': 'datasets (built-in)',
    'anscombe':      'datasets (built-in)',
    'state.region':  'datasets (built-in)',
    'state.name':    'datasets (built-in)',
    'state.x77':     'datasets (built-in)',
    'state.abb':     'datasets (built-in)',
}

# Datasets accessed via library(wooldridge)
WOOLDRIDGE_DATASETS = {'crime2', 'crime4'}

# Datasets accessed via library(Ecdat)
ECDAT_DATASETS = {'Caschool', 'Wages1'}


def extract_code_blocks(filepath, include_comments=False):
    """Return concatenated contents of ```{r} code blocks.

    By default, commented lines (starting with #) are excluded
    so that commented-out code does not produce false positives.
    """
    with open(filepath) as f:
        lines = f.readlines()
    code_lines = []
    in_code = False
    for line in lines:
        s = line.strip()
        if s.startswith('```{r'):
            in_code = True
            continue
        if s.startswith('```') and in_code:
            in_code = False
            continue
        if in_code:
            if not include_comments and s.startswith('#'):
                continue
            code_lines.append(line)
    return ''.join(code_lines)


def find_datasets(filepath):
    """Return sorted list of (dataset_name, source) tuples used in a chapter."""
    code = extract_code_blocks(filepath)
    found = {}  # name -> source

    # 1. data("X") / data('X') / data(X) calls — exclude e.g. make_noisy_data(6)
    for m in re.finditer(r'(?<!\w)data\(\s*["\']?([A-Za-z]\w*)["\']?\s*\)', code):
        name = m.group(1)
        # Determine source from context
        if name in ECDAT_DATASETS:
            found[name] = 'Ecdat'
        elif name in WOOLDRIDGE_DATASETS:
            found[name] = 'wooldridge'
        elif name in BUILTIN_DATASETS:
            found[name] = BUILTIN_DATASETS[name]
        else:
            found[name] = 'data()'

    # 2. read.csv() / read_csv() / read.table()
    for m in re.finditer(
        r'(\w+)\s*<-\s*(?:read\.csv|read_csv|read\.table)\s*\(\s*["\']([^"\']+)["\']',
        code
    ):
        var = m.group(1)
        path = m.group(2)
        # Use filename or URL as source
        if path.startswith('http'):
            label = os.path.basename(path.split('?')[0])
        else:
            label = os.path.basename(path)
        found[var] = f'read.csv ({label})'

    # 3. read_dta()
    for m in re.finditer(
        r'(\w+)\s*<-\s*read_dta\s*\(\s*["\']([^"\']+)["\']', code
    ):
        var = m.group(1)
        path = m.group(2)
        label = os.path.basename(path.split('?')[0])
        found[var] = f'read_dta ({label})'

    # 4. Direct references to known built-in datasets
    for name, source in BUILTIN_DATASETS.items():
        # Use word boundary; state.region needs special escaping
        pattern = re.escape(name)
        if re.search(r'\b' + pattern + r'\b', code):
            if name not in found:
                found[name] = source

    # 5. Wooldridge datasets used directly (after library(wooldridge))
    if re.search(r"library\s*\(\s*['\"]?wooldridge['\"]?\s*\)", code):
        for name in WOOLDRIDGE_DATASETS:
            if re.search(r'\b' + name + r'\b', code):
                if name not in found:
                    found[name] = 'wooldridge'

    # 6. Ecdat datasets used directly (after library(Ecdat))
    if re.search(r"library\s*\(\s*['\"]?Ecdat['\"]?\s*\)", code):
        for name in ECDAT_DATASETS:
            if re.search(r'\b' + name + r'\b', code):
                if name not in found:
                    found[name] = 'Ecdat'

    return sorted(found.items())


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
        '04': '**Appendices**',
    }
    return headers.get(prefix)


if __name__ == '__main__':
    bookdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'book')
    files = sorted(glob.glob(os.path.join(bookdir, '[0-9][0-9]_[0-9][0-9]_*.qmd')))

    # Parse flags
    by_dataset = '--by-dataset' in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    filt = args[0] if args else None

    if filt:
        files = [f for f in files if filt in os.path.basename(f)]

    # Collect results
    results = []  # (filepath, fname, part, label, datasets)
    for fp in files:
        fname = os.path.basename(fp)
        lbl = label_from_filename(fname)
        part = fname[:2]
        datasets = find_datasets(fp)
        results.append((fp, fname, part, lbl, datasets))

    if by_dataset:
        # ── Group by dataset ────────────────────────────────────────────
        ds_map = {}  # (name, source) -> [chapter_labels]
        for fp, fname, part, lbl, datasets in results:
            for name, source in datasets:
                key = (name, source)
                ds_map.setdefault(key, []).append(lbl)

        print('| Dataset | Source | Chapters |')
        print('|---|---|---|')
        for (name, source), chapters in sorted(ds_map.items()):
            ch_list = '; '.join(chapters)
            print(f'| {name} | {source} | {ch_list} |')

    else:
        # ── Group by chapter ────────────────────────────────────────────
        print('| Chapter | Datasets |')
        print('|---|---|')

        prev_part = None
        for fp, fname, part, lbl, datasets in results:
            if part != prev_part and not filt:
                hdr = part_header(part)
                if hdr:
                    print(f'| {hdr} |')
                prev_part = part

            if datasets:
                ds_str = ', '.join(f'{n} ({s})' for n, s in datasets)
            else:
                ds_str = '—'
            print(f'| {lbl} | {ds_str} |')

    # ── Summary ─────────────────────────────────────────────────────────
    all_datasets = {}
    for fp, fname, part, lbl, datasets in results:
        for name, source in datasets:
            all_datasets.setdefault(name, set()).add(source)

    n_chapters = sum(1 for r in results if r[4])
    n_total = len(results)
    print(f'\n{len(all_datasets)} distinct datasets across {n_chapters}/{n_total} chapters')
