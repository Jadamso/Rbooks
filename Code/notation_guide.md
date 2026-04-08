# Notation Guide -- Rbooks

Reference for all mathematical notation used in the textbook. Claude agents writing or editing .qmd files must follow these conventions exactly. Do not rename or restyle existing notation.

---

## Core Principle: Hats and No Hats

The book distinguishes **sample** (observed data) from **population** (theoretical) with hats:

| Concept | Sample (data) | Population (theory) |
|---------|---------------|---------------------|
| Observation | $\hat{X}_i$ | $X_i$ |
| Mean | $\hat{M}$ | $\mu$ or $\mathbb{E}[X_i]$ |
| Variance | $\hat{V}$ | $\sigma^2$ or $\mathbb{V}[X_i]$ |
| Std deviation | $\hat{S}$ | $\sigma$ |
| Probability | $\hat{p}_x$ | $p_x$ |
| Regression coeff | $\hat{b}_k$ | $\beta_k$ |
| Predicted value | $\hat{Y}_i$ or $\hat{y}_i$ | -- |
| Residual | $\hat{e}_i$ | $\epsilon_i$ |

Use $\hat{\cdot}$ for anything computed from data. Use bare Greek or Roman for population/theoretical quantities.

---

## Data and Indices

| Symbol | Meaning | LaTeX |
|--------|---------|-------|
| $\hat{X}_i$ | Value of the $i$th observation | `$\hat{X}_i$` |
| $n$ | Sample size | `$n$` |
| $i$ | Observation index ($i = 1, \ldots, n$) | `$i$` |
| $k$ | Variable index | `$k$` |
| $j$ | Secondary observation index (pairwise sums) | `$j$` |
| $g$ | Group index | `$g$` |
| $K$ | Number of explanatory variables | `$K$` |
| $G$ | Number of groups | `$G$` |

---

## Descriptive Statistics

| Symbol | Meaning | LaTeX |
|--------|---------|-------|
| $\hat{M}$ | Sample mean | `$\hat{M}$` |
| $\hat{V}$ | Sample variance | `$\hat{V}$` |
| $\hat{S}$ | Sample standard deviation | `$\hat{S}$` |
| $\tilde{M}$ | Sample median | `$\tilde{M}$` |
| $\hat{\text{MAD}}$ | Median absolute deviation | `$\hat{\text{MAD}}$` |
| $\hat{IQR}$ | Interquartile range | `$\hat{IQR}$` |
| $W_x$ | Unnormalized weight | `$W_x$` |
| $w_x$ | Normalized weight ($\sum w_x = 1$) | `$w_x$` |

---

## Population Parameters

| Symbol | Meaning | LaTeX |
|--------|---------|-------|
| $\mu$ | Population mean | `$\mu$` |
| $\sigma^2$ | Population variance | `$\sigma^2$` |
| $\sigma$ | Population standard deviation | `$\sigma$` |
| $p$ | Bernoulli/Binomial success probability | `$p$` |
| $\lambda$ | Poisson/Exponential rate parameter | `$\lambda$` |
| $\theta$ | Generic parameter | `$\theta$` |
| $\alpha$ | Significance level (Type I error) | `$\alpha$` |
| $\rho$ | Population correlation | `$\rho$` |

---

## Expectation Operators

Use blackboard bold with **square brackets**:

| Operator | Meaning | LaTeX |
|----------|---------|-------|
| $\mathbb{E}[X_i]$ | Expected value | `$\mathbb{E}[X_i]$` |
| $\mathbb{V}[X_i]$ | Variance | `$\mathbb{V}[X_i]$` |
| $\mathbb{C}[X_i, Y_i]$ | Covariance | `$\mathbb{C}[X_i, Y_i]$` |
| $\mathbb{R}[X_i, Y_i]$ | Correlation | `$\mathbb{R}[X_i, Y_i]$` |
| $\mathbb{E}[X_i \mid Y_i]$ | Conditional expectation | `$\mathbb{E}[X_i \mid Y_i]$` |

**Note:** The book uses square brackets `$\mathbb{V}[\cdot]$` as the standard. Avoid parentheses `$\mathbb{V}(\cdot)$` in new content.

---

## Probability Notation

| Symbol | Meaning | LaTeX |
|--------|---------|-------|
| $Prob(X_i = x)$ | Probability mass/density | `$Prob(X_i = x)$` |
| $Prob(X_i \leq x)$ | Cumulative probability | `$Prob(X_i \leq x)$` |
| $Prob(X_i = x \mid Y_i = y)$ | Conditional probability | `$Prob(X_i = x \mid Y_i = y)$` |
| $F(x)$ | CDF (population) | `$F(x)$` |
| $\hat{F}(x)$ | Empirical CDF (sample) | `$\hat{F}(x)$` |
| $f(x)$ | PDF (continuous) | `$f(x)$` |
| $\mathbf{1}(\cdot)$ | Indicator function | `$\mathbf{1}(\cdot)$` |

Use `$Prob(\cdot)$` as the standard probability function. Avoid `$Pr(\cdot)$` or `$P(\cdot)$` in new content.

---

## Distributions

| Distribution | Notation | Parameters | LaTeX |
|-------------|----------|------------|-------|
| Normal | $N(\mu, \sigma^2)$ | mean, variance | `$N(\mu, \sigma^2)$` |
| Bernoulli | $X_i \in \{0, 1\}$ | $p$ | -- |
| Binomial | $\binom{n}{k} p^k (1-p)^{n-k}$ | $n$, $p$ | `$\binom{n}{k}$` |
| Poisson | $\text{Poisson}(\lambda)$ | $\lambda$ | `$\text{Poisson}(\lambda)$` |
| Uniform | $\text{Uniform}(a, b)$ | $a$, $b$ | `$\text{Uniform}(a,b)$` |
| Student t | $t_{df}$ | degrees of freedom | `$t_{df}$` |
| F | $F_{df_1, df_2}$ | two df parameters | `$F_{df_1, df_2}$` |
| Exponential | $\text{Exp}(\lambda)$ | rate $\lambda$ | `$\text{Exp}(\lambda)$` |

---

## Regression

### Simple regression

$$\hat{Y}_i = b_0 + b_1 \hat{X}_i + e_i$$

### Multiple regression

$$\hat{Y}_i = \sum_{k=0}^{K} b_k \hat{X}_{ik} + e_i$$

| Symbol | Meaning | LaTeX |
|--------|---------|-------|
| $b_0$ | Intercept (sample) | `$b_0$` |
| $b_k$ | Slope coefficient (sample) | `$b_k$` |
| $\hat{b}_k$ | OLS estimate of $b_k$ | `$\hat{b}_k$` |
| $b_k^*$ | Optimal/best-fit coefficient | `$b_k^*$` |
| $\beta_k$ | Population coefficient | `$\beta_k$` |
| $\epsilon_i$ | Population error term | `$\epsilon_i$` |
| $e_i$ | Sample residual | `$e_i$` |
| $\hat{C}_{XY}$ | Sample covariance | `$\hat{C}_{XY}$` |
| $\hat{V}_X$ | Sample variance of X | `$\hat{V}_X$` |
| $\hat{R}^2$ | Coefficient of determination | `$\hat{R}^2$` |
| $\hat{R}^2_{adj}$ | Adjusted R-squared | `$\hat{R}^2_{adj}$` |

### Sums of squares

| Symbol | Meaning | LaTeX |
|--------|---------|-------|
| $\hat{TSS}$ | Total sum of squares | `$\hat{TSS}$` |
| $\hat{ESS}$ | Explained sum of squares | `$\hat{ESS}$` |
| $\hat{RSS}$ | Residual sum of squares | `$\hat{RSS}$` |
| $\hat{BSS}$ | Between-group sum of squares | `$\hat{BSS}$` |
| $\hat{WSS}$ | Within-group sum of squares | `$\hat{WSS}$` |

### Matrix notation (Ch 26)

| Symbol | Meaning | LaTeX |
|--------|---------|-------|
| $\mathbf{X}$ | Design matrix | `$\mathbf{X}$` |
| $\mathbf{Y}$ | Outcome vector | `$\mathbf{Y}$` |
| $\mathbf{X}'$ | Transpose | `$\mathbf{X}'$` |
| $(\mathbf{X}'\mathbf{X})^{-1}$ | Inverse cross-product | `$(\mathbf{X}'\mathbf{X})^{-1}$` |

Use prime `$'$` for transpose, not `$^T$`.

---

## Local Regression and Nonparametrics

| Symbol | Meaning | LaTeX |
|--------|---------|-------|
| $m(x)$ | True conditional mean function | `$m(x)$` |
| $\hat{m}(x)$ | Estimated conditional mean | `$\hat{m}(x)$` |
| $h$ or $h_p$ | Bandwidth | `$h$` or `$h_p$` |
| $K(u)$ | Kernel function | `$K(u)$` |
| $L$ | Number of bins | `$L$` |
| $\hat{b}_0(x, h)$ | Local intercept | `$\hat{b}_0(x,h)$` |
| $\hat{\beta}_p(\mathbf{x})$ | Local marginal effect | `$\hat{\beta}_p(\mathbf{x})$` |
| $\mathbf{H}$ | Bandwidth matrix | `$\mathbf{H}$` |

---

## Hypothesis Testing

| Symbol | Meaning | LaTeX |
|--------|---------|-------|
| $H_0$ | Null hypothesis | `$H_0$` |
| $H_A$ | Alternative hypothesis | `$H_A$` |
| $\hat{t}$ | t-statistic | `$\hat{t}$` |
| $\hat{F}$ | F-statistic | `$\hat{F}$` |
| $\hat{SE}$ | Standard error | `$\hat{SE}$` |
| $s_{\hat{b}_k}$ | SE of regression coefficient | `$s_{\hat{b}_k}$` |
| $q(\alpha/2)$ | Critical quantile | `$q(\alpha/2)$` |
| $z$ | Standard normal score | `$z$` |

---

## Sampling and Resampling

| Symbol | Meaning | LaTeX |
|--------|---------|-------|
| $M$ | Estimator (random variable, pre-data) | `$M$` |
| $\hat{M}$ | Estimate (realized, post-data) | `$\hat{M}$` |
| $SE(M)$ | Standard error of estimator | `$SE(M)$` |
| $\sigma / \sqrt{n}$ | SE formula for the mean | `$\sigma / \sqrt{n}$` |
| $\hat{M}_b^{\text{boot}}$ | Bootstrap replicate mean | `$\hat{M}_b^{\text{boot}}$` |
| $\hat{SE}^{\text{boot}}$ | Bootstrap standard error | `$\hat{SE}^{\text{boot}}$` |
| $\hat{SE}^{\text{jack}}$ | Jackknife standard error | `$\hat{SE}^{\text{jack}}$` |
| $\hat{M}_i^{\text{jack}}$ | Leave-one-out mean | `$\hat{M}_i^{\text{jack}}$` |

---

## ANOVA (Ch 20)

| Symbol | Meaning | LaTeX |
|--------|---------|-------|
| $\hat{Y}_{ig}$ | Observation $i$ in group $g$ | `$\hat{Y}_{ig}$` |
| $\hat{M}_g$ | Group $g$ mean | `$\hat{M}_g$` |
| $\hat{M}_Y$ | Grand mean | `$\hat{M}_Y$` |
| $n_g$ | Group size | `$n_g$` |
| $\hat{D}$ | Difference in means | `$\hat{D}$` |
| $\hat{F}$ | F-statistic | `$\hat{F}$` |
| $F_{G-1, n-G}$ | F-distribution reference | `$F_{G-1, n-G}$` |

---

## Superscript and Subscript Conventions

| Pattern | Meaning | Example |
|---------|---------|---------|
| $_i$ | Observation index | $\hat{X}_i$ |
| $_k$ | Variable index (never $_j$) | $b_k$, $\hat{X}_{ik}$ |
| $_j$ | Secondary observation index (pairwise sums only) | $\hat{X}_j$ in $\sum_{j \neq i}$ |
| $_g$ | Group index | $\hat{M}_g$ |
| $_{x}$ or $_{xy}$ | Outcome value | $\hat{p}_x$, $\hat{p}_{xy}$ |
| $^*$ | Optimal value | $b_k^*$ |
| $^{(b)}$ | Bootstrap replicate | $\hat{X}_i^{(b)}$ |
| $^{\text{boot}}$ | Bootstrap variant | $\hat{SE}^{\text{boot}}$ |
| $^{\text{jack}}$ | Jackknife variant | $\hat{SE}^{\text{jack}}$ |
| $_{[i]}$ | Leave-one-out | $\hat{y}_{[i]}$ |
| $_{\text{null}}$ | Under null hypothesis | $M_{\text{null}}$ |
| $_{\text{obs}}$ | Observed value | $t_{\text{obs}}$ |

---

## Equations Environment

Use `eqnarray` for displayed equations:

```latex
\begin{eqnarray}
\hat{M} &=& \frac{\sum_{i=1}^{n} \hat{X}_i}{n}
\end{eqnarray}
```

Do not use `align`, `equation`, or `gather`. The book uses `eqnarray` throughout.

---

## Quick Rules

1. **Hats on data**: $\hat{X}_i$, $\hat{M}$, $\hat{V}$, $\hat{b}_k$ for anything computed from a sample.
2. **Greek for population**: $\mu$, $\sigma$, $\beta_k$, $\epsilon_i$.
3. **Blackboard bold operators**: $\mathbb{E}$, $\mathbb{V}$, $\mathbb{C}$, $\mathbb{R}$ with square brackets.
4. **Probability**: Write `$Prob(\cdot)$`, not `$P(\cdot)$` or `$Pr(\cdot)$`.
5. **Transpose**: Use prime `$'$`, not `$^T$`.
6. **Equations**: Use `\begin{eqnarray}...\end{eqnarray}`.
7. **Variable index**: Use `$_k$` for variables, never `$_j$`. Reserve `$_j$` for secondary observation indices in pairwise sums.
8. **Do not rename**: If a symbol already exists in the book, use the existing form. Check this guide first.
