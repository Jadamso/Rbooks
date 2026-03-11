# CLAUDE.md — Rbooks

## Project Overview

**Introductory Economic Statistics: A Data-Driven Approach using R**
A Quarto book used in Stats I, Stats II, and Econometrics courses at TRU.

- Live site: https://jadamso.github.io/Rbooks/
- Source: https://github.com/Jadamso/Rbooks

## Directory Structure

```
book/        # Source .qmd files (edit these)
  _quarto.yml
docs/        # Rendered output (auto-generated, do not hand-edit)
  *.html
book/_freeze/ # Cached chunk outputs (tracked on main; do not delete casually)
ToDo.md      # Ongoing task list — check this for current priorities
```

## Book Structure

| Part | Topic | File prefix |
|------|-------|-------------|
| 0 | Getting Started | `00_` |
| 1 | Univariate Data (Stats I) | `01_` |
| 2 | Bivariate Data (Stats II) | `02_` |
| 3 | Multivariate Data (Econometrics) | `03_` |

Chapter files follow `PP_NN_Title.qmd` naming. The TOC is defined in `book/_quarto.yml`.

## Workflow

```bash
# Preview locally (live reload)
quarto preview book

# Full render to docs/
quarto render book

# Publish (current method — render first, then push)
quarto render book
cp -r ./Templates/Figures_Manual/* ./docs/Figures_Manual
git add . && git commit -m "message" && git push
```

**Planned migration**: Move deployment to `gh-pages` branch so `docs/` is no longer tracked on `main`. See `ToDo.md` for the step-by-step plan.

## Key Conventions

- All source edits go in `book/*.qmd`
- `output-dir: ../docs` in `_quarto.yml` — rendered HTML lands in `docs/`
- `freeze: auto` — chunk outputs are cached in `book/_freeze/`; only re-execute on change
- After renaming/deleting chapters, clean stale freeze dirs:
  ```bash
  cd book && for d in _freeze/*/; do stem=$(basename "$d"); [ ! -f "${stem}.qmd" ] && rm -rf "$d"; done
  ```
- Do not modify `docs/` by hand
- Do not delete `_freeze/` entries without checking if the source chapter still exists

## Callout Conventions

- **Must Know**: `::: {.callout-tip icon=false collapse="true"}`
- **Test Yourself**: `::: {.callout-note icon=false collapse="true"}`
- **Warning/Important**: `.callout-warning` / `.callout-important`

## Git Conventions

- Commit messages: concise, one line (no multi-paragraph descriptions)
- Do not add Co-Authored-By lines

## Current Priorities (from ToDo.md)

1. **gh-pages migration** — eliminates `docs/` bloat on `main`
2. **Content depth** — numerical examples for every math expression; 3 end-of-chapter questions per chapter
3. **Callouts** — add definition callouts to Univariate Data; propagate to other parts
4. **Writing** — consistent section/subsection style; clean up figures (axes, titles, legends)
5. **Harmonize notation** — bandwidth `h` used consistently across histograms, local regression, KDE
