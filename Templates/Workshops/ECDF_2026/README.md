# ECDF, Bootstrap, and AI Reviewer workshop

A lecture and lab for colleagues, built from Chapters 2, 5, and 7 and Appendix A of the book.

| File | Purpose |
|---|---|
| `ECDF_Bootstrap.R` | The standalone R lab script participants run in RStudio (base R, `wooldridge::wage2`, runs in a few seconds) |
| `Slides.qmd` | The lecture slides (revealjs), which execute the same code and extend the `wage2` example to rural vs urban and education-group comparisons, plus a Canada-USA income comparison |
| `Handout.qmd` | Step-by-step lab instructions, including the Claude prompts |
| `income_lis_2020.csv` | Canada/USA market and disposable income deciles for 2020, from LIS via Our World in Data |
| `Build_Income_Comparison.R` | Download the published income thresholds and rebuild the compact income CSV using base R |

Render the materials with `quarto render Slides.qmd` and `quarto render Handout.qmd` from this folder.
The rendered HTML files are self-contained and can be emailed as-is.
They are not stored in this repository.
Only the slides read a CSV file in this folder (`income_lis_2020.csv`).
The main example (`wage2`) and the optional CEO salary exercise (`ceosal1`) both use the `wooldridge` package.

The income comparison uses the [LIS June 2026 release, processed by Our World in Data](https://www.lisdatacenter.org/data-access/lis-in-our-world-in-data-owid/), downloaded 15 September 2026 from its [income distribution explorer](https://ourworldindata.org/explorers/incomes-across-distribution-lis).
Both countries use annual household income divided by the square root of household size, weighted by people, in 2021 international dollars adjusted for purchasing power and inflation.
Market income excludes public transfers and precedes income taxes and social contributions; disposable income includes public transfers and deducts those taxes and contributions.
The measures include recorded cash and noncash income components, without valuing all public services.
The CSV contains P10 through P90 thresholds, so the plots interpolate between these points and omit the tails.
Run `Rscript Build_Income_Comparison.R` to refresh the CSV; later source revisions may change the values.

The CC0 dedication for this repository covers the slides, handout, and scripts.
The income CSV is derived from LIS data published by Our World in Data and keeps the terms of those sources.
