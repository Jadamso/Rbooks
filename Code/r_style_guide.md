# R Style Guide -- Rbooks

Reference conventions for R code in the textbook. Claude agents writing or editing R code chunks in .qmd files must follow these rules.

---

## Assignment and Naming

- **Always use `<-`** for assignment, never `=`.
- **snake_case** for multi-word names: `sample_means`, `boot_se`, `col_high`.
- **Capital letters** for mathematical objects: `X`, `Y`, `M` (mean), `V` (variance).
- **Short lowercase** for loop indices and counts: `i`, `n`, `b`, `h`.
- **Coefficients**: `b0`, `b1`, `b_k` matching the book's notation.

```r
X <- USArrests[,'Murder']
X_mean <- mean(X)
sample_means <- numeric(B)
```

---

## Base R Only

- Use base R. No tidyverse verbs (`mutate`, `filter`, `select`, `arrange`).
- No native pipe `|>`. Avoid `%>%` except where a package requires chaining (e.g., `plotly`).
- Use `aggregate()`, `subset()`, `merge()`, and bracket indexing instead.
- Access packages via `::` when used once or twice: `car::vif(reg)`. Use `library()` only when a package is used repeatedly in a chapter.

---

## Data Access

- **Bracket notation** `[,'Name']` for subsetting columns by name.
- **Dollar sign** `$` for quick single-column access in inline expressions.
- **Double brackets** `[[]]` for list element extraction.

```r
xy <- USArrests[,c('Murder','UrbanPop')]
x <- xy[,'UrbanPop']
y <- xy[,'Murder']

# also acceptable for single columns
assault_high <- USArrests$Assault > median(USArrests$Assault)
```

---

## Functions

- Opening brace on same line as `function()`.
- Body indented (2 or 4 spaces, match surrounding code).
- Explicit `return()` at the end.
- Closing brace on its own line.

```r
skewness <- function(X) {
    X_mean <- mean(X)
    m3 <- mean((X - X_mean)^3)
    s3 <- sd(X)^3
    skew <- m3 / s3
    return(skew)
}
```

---

## Comments

- Use `#` with a space after: `# comment`.
- Inline comments explain purpose or expected result.

```r
X <- rnorm(1000)        # simulated data
X_mean <- mean(X)       # sample mean
```

---

## Spacing and Formatting

- Spaces around binary operators: `x <- y + 1`, `a * b`.
- Spaces after commas: `c(1, 2, 3)`, `f(x, y)`, `X[1, 2]`, `grey(0, .5)`.
- No spaces inside parentheses: `mean(X)` not `mean( X )`.

---

## Strings

- **Single quotes** throughout: column names, package names, labels, axis text.

```r
USArrests[, 'Murder']
library('wooldridge')
xlab = 'Murder arrests (per 100k)'
```

---

## Simulation and Loops

- `set.seed()` before any random generation block; place at the start of the chunk.
- Never reset `set.seed` mid-chunk.
- `replicate()` for repeated simulations returning a vector/matrix.
- `sapply()` / `lapply()` for apply-style iteration.
- Explicit `for` loops when the iteration is pedagogically important.
- Pre-allocate vectors with `rep(NA, n)`, not `vector(length=n)` or `numeric(n)`.

```r
set.seed(1)
B <- 999
sample_means <- rep(NA, B)
for (b in seq(B)) {
    x_boot <- sample(X, replace=TRUE)
    sample_means[b] <- mean(x_boot)
}
```

---

## Formulas

- Standard R formula syntax: `y ~ x` with spaces around `~`.
- Use in `lm()`, `aov()`, `plot()`, `boxplot()`.
- Interaction: `y ~ x1 * x2`.

```r
reg <- lm(y ~ x, data=xy)
plot(y ~ x, xy, pch=16, col=grey(0, .5))
```

---

## Output Formatting

- `round()` for display precision: `round(value, 2)`.
- `paste0()` for string concatenation in titles and labels.
- Rely on auto-print; avoid explicit `print()` unless inside a loop or conditional.

```r
title(paste0('mean= ', round(X_mean, 2)), font.main=1)
```

---

## Code Chunk Options

- Use comma-separated options in the chunk header: `` ```{r, eval=F} ``.
- Common options: `eval=F`, `echo=F`, `fig.height=10`, `fig.width=10`, `fig.align="center"`.
- Global defaults are set in `_quarto.yml` (`echo: true`, `warning: false`, `message: false`, `collapse: true`).

---

## Quick Rules

1. `<-` for assignment, never `=`.
2. Base R only -- no tidyverse, no pipes.
3. `library()` for repeated use, `pkg::fun()` for one-off calls.
4. Bracket notation `[,'Name']` for column subsetting.
5. Explicit `return()` in all custom functions.
6. `set.seed()` once at the top of a chunk, never reset.
7. Single quotes for all strings.
8. Pre-allocate with `rep(NA, n)`, not `vector(length=n)`.
9. Comments explain purpose, not mechanics.
