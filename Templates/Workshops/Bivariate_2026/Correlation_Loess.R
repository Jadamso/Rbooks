# Lab: correlation, regressograms, and loess with resampling
# Faculty workshop, Thompson Rivers University, 2026
# Code companion to Handout.qmd, in the same order as the lab.
#
# Write three sentences here about the statistical ideas before the AI review.
# 1.
# 2.
# 3.
#
# Companion chapters in "Introductory Economic Statistics" (https://jadamso.github.io/Rbooks/):
#   Statistics of Association (Ch. 14) for the correlation, its bootstrap, and permutation tests,
#   Simple Regression (Ch. 15) for the least squares line,
#   Local Regression (Ch. 17) for regressograms,
#   Gradients (Ch. 18) for loess and bootstrap confidence bands.
#
# How to run in RStudio: Session > Restart R, then Source with Echo.
# Only base R is used, plus the wage1 data from the wooldridge package.
# Install the package once with install.packages('wooldridge').

set.seed(1) # one seed at the top makes every simulation below replicable

# Data: 526 US workers from the 1976 Current Population Survey
xy_hat <- wooldridge::wage1[, c('exper', 'wage')]
colnames(xy_hat) <- c('x_hat', 'y_hat') # x_hat=years of potential experience, y_hat=hourly wage (1976 dollars)
n <- nrow(xy_hat)

# Number of resamples, used in every loop below
B <- 999

# R-squared: the squared correlation between wages and fitted wages
r_squared <- function(y, y_fit) {
    cor(y, y_fit)^2
}

# One color per model in every figure: correlation and linear regression (red), regressogram (green), loess (blue)
# Fitted values use the full color, and confidence intervals use a lighter shade of it
fit_cols <- c(linear=rgb(.8, 0, 0, .8), rgram=rgb(0, .6, 0, .8), loess=rgb(0, 0, .8, .8))
ci_cols <- c(linear=rgb(.8, 0, 0, .3), rgram=rgb(0, .6, 0, .3), loess=rgb(0, 0, .8, .3))



### Part 1: Correlation and simple linear regression ###

# Scatterplot, with the least squares line in red
plot(y_hat ~ x_hat, data=xy_hat, pch=16, col=grey(0, .25), main=NA,
    xlab='Years of potential experience', ylab='Hourly wage (1976 dollars)')
# Simple linear regression: the least squares line
reg <- lm(y_hat ~ x_hat, data=xy_hat)
abline(reg, col=fit_cols['linear'], lwd=2)
coef(reg)

# Pearson correlation
xy_cor <- cor(xy_hat[, 'x_hat'], xy_hat[, 'y_hat'])
xy_cor
# The slope is the correlation times the ratio of standard deviations
xy_cor * sd(xy_hat[, 'y_hat']) / sd(xy_hat[, 'x_hat'])
# The squared correlation is the R-squared of the line
xy_cor^2
r_squared(xy_hat[, 'y_hat'], predict(reg))

# Bootstrap distribution of the correlation and the slope
boot_cor <- rep(NA, B)
boot_slope <- rep(NA, B)
for (b in 1:B) {
    # Resample workers with replacement, keeping each worker's experience and wage together
    xy_b <- xy_hat[sample(n, replace=TRUE), ]
    boot_cor[b] <- cor(xy_b[, 'x_hat'], xy_b[, 'y_hat'])
    boot_slope[b] <- coef(lm(y_hat ~ x_hat, data=xy_b))[2]
}

# Percentile confidence interval: the middle 95% of bootstrap correlations
boot_ci <- quantile(boot_cor, probs=c(.025, .975))
boot_ci
# The same for the slope, in dollars per hour for each year of experience
slope_ci <- quantile(boot_slope, probs=c(.025, .975))
slope_ci

# Histogram of bootstrap correlations, with the observed value in red and the interval in light red
hist(boot_cor, breaks=50, border=NA, freq=FALSE, main=NA,
    xlab='Bootstrap correlation')
abline(v=boot_ci, col=ci_cols['linear'], lwd=2)
abline(v=xy_cor, col=fit_cols['linear'], lwd=2)

# Permutation distribution of the correlation, imposing no association
perm_cor <- rep(NA, B)
for (b in 1:B) {
    # Shuffle experience without replacement, which breaks the pairing with wages
    xy_p <- xy_hat
    xy_p[, 'x_hat'] <- sample(xy_hat[, 'x_hat'], replace=FALSE)
    perm_cor[b] <- cor(xy_p[, 'x_hat'], xy_p[, 'y_hat'])
}

# Two-sided p-value: share of permutations at least as extreme as observed
p_cor <- mean(abs(perm_cor) >= abs(xy_cor))
p_cor

# Histogram of permuted correlations, with the observed value in red
hist(perm_cor, breaks=50, border=NA, freq=FALSE, main=NA,
    xlab='Permuted correlation')
abline(v=xy_cor, col=fit_cols['linear'], lwd=2)



### Part 2: A regressogram ###

# Ten-year experience bins, so the half-width is h=5
# The last bin is one year wider, so it also holds the one worker with 51 years
bin_breaks <- c(0, 10, 20, 30, 40, 51)
xy_hat[, 'bin'] <- cut(xy_hat[, 'x_hat'], breaks=bin_breaks)
table(xy_hat[, 'bin'])

# Regressogram: the mean wage in each bin
bin_means <- tapply(xy_hat[, 'y_hat'], xy_hat[, 'bin'], mean)
bin_means
# The same means are the coefficients from OLS on one dummy per bin, with no intercept
rgram <- lm(y_hat ~ 0 + bin, data=xy_hat)
coef(rgram)
rgram_r2 <- r_squared(xy_hat[, 'y_hat'], predict(rgram))
rgram_r2

# Bootstrap distribution of each bin mean, one row per resample
boot_bins <- matrix(NA, nrow=B, ncol=length(bin_means))
colnames(boot_bins) <- names(bin_means)
for (b in 1:B) {
    # Resample workers with replacement, then recompute the mean in each bin
    xy_b <- xy_hat[sample(n, replace=TRUE), ]
    boot_bins[b, ] <- tapply(xy_b[, 'y_hat'], xy_b[, 'bin'], mean)
}

# Percentile confidence interval for each bin mean, one column per bin
bin_ci <- apply(boot_bins, 2, quantile, probs=c(.025, .975))
round(bin_ci, 2)

# Scatterplot with the bin means in green and their intervals in light green
plot(y_hat ~ x_hat, data=xy_hat, pch=16, col=grey(0, .25), main=NA,
    xlab='Years of potential experience', ylab='Hourly wage (1976 dollars)')
bin_lower <- bin_breaks[-length(bin_breaks)]
bin_upper <- bin_breaks[-1]
rect(bin_lower, bin_ci[1, ], bin_upper, bin_ci[2, ], col=ci_cols['rgram'], border=NA)
segments(bin_lower, bin_means, bin_upper, bin_means, col=fit_cols['rgram'], lwd=2)

# Permutation distribution of the regressogram R-squared, imposing no association
perm_rgram_r2 <- rep(NA, B)
for (b in 1:B) {
    # Shuffle experience, then recompute each worker's bin from the shuffled value
    xy_p <- xy_hat
    xy_p[, 'x_hat'] <- sample(xy_hat[, 'x_hat'], replace=FALSE)
    xy_p[, 'bin'] <- cut(xy_p[, 'x_hat'], breaks=bin_breaks)
    rgram_p <- lm(y_hat ~ 0 + bin, data=xy_p)
    perm_rgram_r2[b] <- r_squared(xy_p[, 'y_hat'], predict(rgram_p))
}

# One-sided p-value, since R-squared is never negative
# A value of 0 means no permutation reached the observed value, so p < 1/B
p_rgram <- mean(perm_rgram_r2 >= rgram_r2)
p_rgram

# Histogram of permuted R-squared values, with the observed value in green
hist(perm_rgram_r2, breaks=50, border=NA, freq=FALSE, main=NA,
    xlim=range(c(perm_rgram_r2, rgram_r2)),
    xlab='Permuted regressogram R-squared')
abline(v=rgram_r2, col=fit_cols['rgram'], lwd=2)



### Part 3: Loess ###

# Local linear loess with the default span, which uses the nearest 75% of workers at each x
reg_lo <- loess(y_hat ~ x_hat, data=xy_hat, degree=1)
lo_r2 <- r_squared(xy_hat[, 'y_hat'], predict(reg_lo))
lo_r2

# Predict at every year of experience in the data
pred_design <- data.frame(x_hat=seq(min(xy_hat[, 'x_hat']), max(xy_hat[, 'x_hat'])))
y_fit_lo <- predict(reg_lo, newdata=pred_design)
# Experience at the peak of the fitted curve
pred_design[which.max(y_fit_lo), 'x_hat']

# Bootstrap distribution of the loess curve, one column per resample
boot_lo <- matrix(NA, nrow=nrow(pred_design), ncol=B)
for (b in 1:B) {
    # Resample workers with replacement, refit loess, and predict at every design point
    xy_b <- xy_hat[sample(n, replace=TRUE), ]
    reg_lo_b <- loess(y_hat ~ x_hat, data=xy_b, degree=1)
    boot_lo[, b] <- predict(reg_lo_b, newdata=pred_design)
}

# Pointwise 95% confidence band
# Loess does not extrapolate, so a resample that misses the most experienced workers gives NA there
lo_cb <- apply(boot_lo, 1, quantile, probs=c(.025, .975), na.rm=TRUE)

# Scatterplot with the loess curve in blue and its band in light blue
plot(y_hat ~ x_hat, data=xy_hat, pch=16, col=grey(0, .25), main=NA,
    xlab='Years of potential experience', ylab='Hourly wage (1976 dollars)')
polygon(c(pred_design[, 'x_hat'], rev(pred_design[, 'x_hat'])),
    c(lo_cb[1, ], rev(lo_cb[2, ])), col=ci_cols['loess'], border=NA)
lines(pred_design[, 'x_hat'], y_fit_lo, col=fit_cols['loess'], lwd=2)

# Permutation distribution of the loess R-squared, imposing no association
perm_lo_r2 <- rep(NA, B)
for (b in 1:B) {
    # Shuffle experience without replacement, then refit loess
    xy_p <- xy_hat
    xy_p[, 'x_hat'] <- sample(xy_hat[, 'x_hat'], replace=FALSE)
    reg_lo_p <- loess(y_hat ~ x_hat, data=xy_p, degree=1)
    perm_lo_r2[b] <- r_squared(xy_p[, 'y_hat'], predict(reg_lo_p))
}

# One-sided p-value, as for the regressogram
p_lo <- mean(perm_lo_r2 >= lo_r2)
p_lo

# Histogram of permuted R-squared values, with the observed value in blue
hist(perm_lo_r2, breaks=50, border=NA, freq=FALSE, main=NA,
    xlim=range(c(perm_lo_r2, lo_r2)),
    xlab='Permuted loess R-squared')
abline(v=lo_r2, col=fit_cols['loess'], lwd=2)

# Summary: the same two loops for three descriptions of the data
round(cbind(
    R_squared=c(Linear=xy_cor^2, Regressogram=rgram_r2, Loess=lo_r2),
    p_value=c(p_cor, p_rgram, p_lo)), 3)



### Part 4: Scripting and AI ###

# Save a working copy as Correlation_Loess.R.
# Fill in the three summary sentences at the top, then change one comment and note its line.
# Follow the steps in Handout.qmd to review, revise, and convert your script to Quarto.



### Extension: marginal effects ###

# The marginal effect of experience at x is the slope of the loess curve from Part 3 at x.
# The linear regression coefficient is neither the mean marginal effect nor the marginal effect at the mean.

# Slope of a loess curve at x, from a small step on each side of x
# At the edges of the data the curve was fit to, the step uses only the side inside the data
lo_slope <- function(lo_fit, x, eps=.01) {
    x_range <- range(lo_fit[['x']])
    x_lo <- pmax(x - eps, x_range[1])
    x_hi <- pmin(x + eps, x_range[2])
    y_lo <- predict(lo_fit, newdata=data.frame(x_hat=x_lo))
    y_hi <- predict(lo_fit, newdata=data.frame(x_hat=x_hi))
    (y_hi - y_lo) / (x_hi - x_lo)
}

# Mean marginal effect: the slope at each worker's experience, averaged over workers
me_mean <- mean(lo_slope(reg_lo, xy_hat[, 'x_hat']))
me_mean
# Marginal effect at the mean: the slope at the mean experience
me_at_mean <- lo_slope(reg_lo, mean(xy_hat[, 'x_hat']))
me_at_mean
# Compare with the linear regression coefficient from Part 1
coef(reg)[2]

# Bootstrap both marginal effects: resample workers, refit loess, and recompute each one
boot_me <- matrix(NA, nrow=B, ncol=2)
for (b in 1:B) {
    xy_b <- xy_hat[sample(n, replace=TRUE), ]
    reg_lo_b <- loess(y_hat ~ x_hat, data=xy_b, degree=1)
    boot_me[b, 1] <- mean(lo_slope(reg_lo_b, xy_b[, 'x_hat']))
    boot_me[b, 2] <- lo_slope(reg_lo_b, mean(xy_b[, 'x_hat']))
}

# Percentile confidence interval for each, one column per marginal effect
me_ci <- apply(boot_me, 2, quantile, probs=c(.025, .975))
colnames(me_ci) <- c('Mean marginal effect', 'Marginal effect at the mean')
round(me_ci, 3)
# The same interval for the linear regression coefficient, from Part 1
round(slope_ci, 3)
