# Lab: the ECDF and a bootstrap CI for the median
# Faculty workshop, Thompson Rivers University, September 2026
# Code companion to Handout.qmd, in the same order as the lab.
#
# Write three sentences here about the statistical ideas before the AI review.
# 1.
# 2.
# 3.
#
# Companion chapters in "Introductory Economic Statistics" (https://jadamso.github.io/Rbooks/):
#   Data (Ch. 2) for the ECDF and quantiles,
#   Sampling (Ch. 5) for the bootstrap,
#   Intervals (Ch. 7) for bootstrap confidence intervals.
#
# How to run in RStudio: Session > Restart R, then Source with Echo.
# Only base R is used, plus the wage2 data from the wooldridge package.
# Install the package once with install.packages('wooldridge').

set.seed(1) # one seed at the top makes every simulation below replicable



### Part 1: The empirical CDF ###

# Tiny sample to read by hand
X_tiny <- c(2, 3.1, 0.01)
# ECDF of the tiny sample
plot(ecdf(X_tiny), main=NA, pch=16, col=grey(0, .5),
    xlab='x', ylab='Proportion at or below x')
# Tick marks at each observation
rug(X_tiny)

# Data: monthly earnings (1980 dollars) of 935 US workers, Blackburn and Neumark (1992)
X <- wooldridge::wage2[, 'wage']
# Data summary
F_hat <- ecdf(X)
plot(F_hat, main=NA, pch=16, col=grey(0, .5),
    xlab='Monthly earnings (1980 dollars)',
    ylab='Proportion of workers at or below x')

# Proportion of Data <= 1000
mean(X <= 1000) # Direct calculation
F_hat(1000)     # using the ECDF
# Value of x at which 62% of data are <= x
quantile(F_hat, probs=.62, type=1)  # Invert the ECDF

# ECDF of monthly earnings
plot(F_hat, main=NA, pch=16, col=grey(0, .5),
    xlab='Monthly earnings (1980 dollars)',
    ylab='Proportion of workers at or below x')
# Blue line from 0.62 across to the ECDF, then down to 1000
segments(-500, 0.62, 1000, 0.62, col=rgb(0, 0, 1, .8))
segments(1000, 0, 1000, 0.62, col=rgb(0, 0, 1, .8))



### Part 2: A bootstrap confidence interval for the median ###

# single random draw from F_hat
sample(X, 1)

# Bootstrap sample
X_1 <- sample(X, replace=TRUE)
median(X_1)
# Another Bootstrap sample
X_2 <- sample(X, replace=TRUE)
median(X_2)

# Number of bootstrap samples
B <- 9999
# Empty vector to hold the bootstrap medians
boot_medians <- rep(NA, B)
# Fill the vector in a loop
for (b in 1:B) {
    # Resample the data with replacement, then store the median
    X_b <- sample(X, replace=TRUE)
    boot_medians[b] <- median(X_b)
}

# Percentile confidence interval: the middle 95% of bootstrap medians
boot_ci <- quantile(boot_medians, probs=c(.025, .975))
boot_ci

# Histogram of bootstrap medians, with the interval in blue
hist(boot_medians, main=NA, xlab='Bootstrap median')
abline(v=boot_ci, col='blue', lwd=2)

# Compare with the normal-approximation interval requested in Things to try
# The theoretical SE below assumes normally distributed observations
n <- length(X)
X_median <- median(X)
X_median
se_normal <- sqrt(pi / 2) * sd(X) / sqrt(n)
se_normal
X_median + c(-1, 1) * 1.96 * se_normal


### Part 3: Scripting and AI ###

# Save a working copy as ECDF_Bootstrap.R.
# Fill in the three summary sentences at the top, then change one comment and note its line.
# Follow the four steps in Handout.qmd to review, revise, and convert your script to Quarto.
