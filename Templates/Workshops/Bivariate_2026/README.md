# Modern regression methods for economists

A lecture and lab for colleagues, built from Chapters 14 to 17 and Appendix A of the book.
It follows the ECDF and bootstrap workshop and reuses its resampling loop for bivariate data.

| File | Purpose |
|---|---|
| `Correlation_Loess.R` | The standalone R lab script participants run in RStudio (base R, `wooldridge::wage1`, runs in a few seconds) |
| `Slides.qmd` | The lecture slides (revealjs), which execute the same code as the lab script |
| `Handout.qmd` | Step-by-step lab instructions, including the Claude prompts |

Render the materials with `quarto render Slides.qmd` and `quarto render Handout.qmd` from this folder.
The rendered HTML files are self-contained and can be emailed as-is.
They are not stored in this repository.

The data are `wage1` from the `wooldridge` package: 526 US workers from the 1976 Current Population Survey.
The lab relates average hourly earnings (`wage`, in 1976 dollars) to years of potential experience (`exper`).
The correlation is weak, but a regressogram and a loess curve both show wages rising and then falling with experience.
Every interval comes from resampling workers with replacement, and every p-value comes from shuffling experience without replacement.

The script, slides, and handout all set the seed once at the top and run the same computations in the same order.
They therefore print the same numbers.

The CC0 dedication for this repository covers the slides, handout, and script.
