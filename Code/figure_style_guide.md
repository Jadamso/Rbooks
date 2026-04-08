# Figure Style Guide -- Rbooks

Reference conventions derived from Chapter 3 (`01_03_DescriptiveStatistics.qmd`) and verified across the full book. Claude agents producing or editing R figures should follow these rules.

## Histograms

```r
hist(X, breaks=25, border=NA, freq=F, main=NA, xlab="label")
```

| Argument   | Convention                  | Notes                                    |
|------------|-----------------------------|------------------------------------------|
| `border`   | `NA`                        | Never use visible borders on bars        |
| `freq`     | `F`                         | Density scale (not counts)               |
| `main`     | `NA` or omit                | Add titles via `title()` instead         |
| `breaks`   | 20--60 integer              | Adjust to sample size; 25 is a good default |
| `col`      | Default (grey) or `grey(0, alpha)` | Use transparency for overlays     |
| `xlab`     | Short descriptive string    | Use `expression()` for math notation     |

## Scatterplots

```r
plot(y ~ x, pch=16, col=grey(0, .5), data=dat, main=NA, xlab="x", ylab="y")
```

| Argument | Convention                        | Notes                                 |
|----------|-----------------------------------|---------------------------------------|
| `pch`    | `16` (solid circle)               | Standard throughout the book          |
| `col`    | `grey(0, alpha)`                  | Alpha in [0.05, 0.5] depending on n  |
| `main`   | `NA` or omit                      | Titles via `title()` if needed        |
| `cex`    | Reduce for large n (e.g., `.5`)   | Default is fine for small datasets    |

### Transparency guide

| Sample size | Suggested alpha |
|-------------|-----------------|
| n < 100     | 0.5             |
| 100--1000   | 0.25            |
| 1000--10000 | 0.1             |
| n > 10000   | 0.05            |

## Titles

Use `title()` after the plot call, not `main=` inside the plot call.

```r
title(paste0('mean= ', round(m, 2)), font.main=1)
```

- `font.main=1` (plain text, not bold) -- always specify this.
- Keep title text short: a statistic value or one-phrase description.
- For multi-panel figures, use `title("label", outer=TRUE)`.

## Colors

### Primary system: grey transparency

- Scatterpoints: `grey(0, alpha)` with first argument always `0`.
- Histogram fill (overlays): `grey(0, .2)` or similar.

### Emphasis colors: rgb()

| Code                    | Color | Use for                              |
|-------------------------|-------|--------------------------------------|
| `rgb(1, 0, 0, .8)`     | Red   | Means, fitted lines, key statistics  |
| `rgb(0, 0, 1, .8)`     | Blue  | SD bounds, secondary reference lines |
| `rgb(0, 0, 0, .8)`     | Black | Horizontal/vertical reference lines  |

Use `rgb()` with an explicit alpha channel rather than numeric codes (`col=2`) or named colors (`"red"`).

### Multi-group colors

For 2 groups: `cols <- c(rgb(.8, 0, 0, .5), rgb(0, 0, .8, .5))`

For 3+ groups: `cols <- hcl.colors(k, alpha=.45)` where `k` is the number of groups.

## Reference Lines

```r
# Vertical line at a statistic (e.g., mean)
abline(v=value, col=rgb(1, 0, 0, .8), lwd=2)

# Horizontal reference (e.g., zero line)
abline(h=0, col=rgb(0, 0, 0, .8), lty=2)

# Confidence interval bounds
abline(v=ci_bounds, col=rgb(0, 0, 1, .8), lty=2)
```

| Element              | col                    | lwd | lty |
|----------------------|------------------------|-----|-----|
| Sample statistic     | `rgb(1, 0, 0, .8)`    | `2` | `1` |
| CI / theoretical     | `rgb(0, 0, 1, .8)`    | `1` | `2` |
| Subtle reference     | `grey(0.5)`            | `1` | `3` |

## Text Annotations

```r
text(x, y, label, col=rgb(0, 0, 1, .8), adj=0)
```

- Use `expression()` or `bquote()` for math: `expression(bar(X) + s[X])`.
- `adj=0` for left-aligned, `adj=0.5` for centered.
- Match `col` to the element being labeled.

## Multi-Panel Layouts

```r
par(mfrow=c(rows, cols))
```

- 2 panels side-by-side: `par(mfrow=c(1,2))`
- 3 panels side-by-side: `par(mfrow=c(1,3))`
- Grid: `par(mfrow=c(2,2))`
- Custom margins: `par(mar=c(4, 4, 1, 1))` -- small top/right margins.

Do not forget to reset `par()` if saving/restoring state:
```r
op <- par(no.readonly=TRUE)
on.exit(par(op), add=TRUE)
```

## Fitted / Overlay Lines

```r
lines(x_sorted, y_hat, col=rgb(1, 0, 0, .8), lwd=2)
```

- Draw fitted lines with `lines()`, not `curve()`.
- `col=rgb(1, 0, 0, .8), lwd=2` for the primary fit.
- `col=rgb(0, 0, 1, .8), lwd=1, lty=2` for comparison/alternative fits.

## Legends

```r
legend("topright", legend=c("A", "B"),
    col=c(rgb(1, 0, 0, .8), rgb(0, 0, 1, .8)), lwd=2, cex=.8)
```

- Position: `"topright"` or `"topleft"` (string, not coordinates).
- `bty='n'` to remove legend box when it clutters the plot.
- Keep entries short (1--3 words each).
- Match legend symbols to plot symbols (`lty=`, `pch=`, `col=`).

## Boxplots

```r
boxplot(X1, X2, names=c("A", "B"), main=NA, xlab="Groups")
```

- Use `main=NA`; add titles with `title(..., font.main=1)`.
- For colored boxplots by group, use `col=hcl.colors(k, alpha=.45)`.
- Use `border="white"` or `border=NA` when fill color is specified.

## Quick Checklist

Before committing a figure, verify:

- [ ] `border=NA` on all histograms
- [ ] `freq=F` for density histograms
- [ ] `pch=16` for scatterplots
- [ ] `grey(0, alpha)` for point transparency
- [ ] `font.main=1` if title is used
- [ ] `rgb()` with alpha for emphasis colors (not `col=2` or `"red"`)
- [ ] Axis labels present (`xlab`, `ylab`)
- [ ] No bold titles (no default `font.main=2`)
- [ ] Multi-panel layouts use `par(mfrow=...)`, not `layout()`
