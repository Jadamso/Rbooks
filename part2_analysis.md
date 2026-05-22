# Part 2 Analysis — Bivariate Data (Stats II)

Phase 1 reading notes. Covers all 9 Part 2 chapters plus context from Part 1
(`01_02`, `01_03`, `01_05`, `01_06`, `01_07`, `01_08`) and Part 3 (`03_19`,
`03_21`). No edits made during this phase.

---

## Conventions students arrive with (from Part 1)

- **Data types** (`01_02`): cardinal vs factor; histogram density with bin
  half-width `h`; ECDF $\hat{F}(x)$; quantiles; kernel density with uniform
  kernel $k_U$ and bandwidth $h$.
- **Descriptive stats** (`01_03`): $\hat{M}$, $\hat{V}$, $\hat{S}$, median
  $\tilde{M}$, $\hat{IQR}$, $\hat{\text{MAD}}$, weighted mean, skew, kurtosis.
- **Sampling** (`01_05`): population/sample, sampling distribution, LLN, CLT,
  jackknife and bootstrap distributions, $\hat{SE}^{\text{boot}}$,
  $\hat{SE}^{\text{jack}}$ (rescaled by $\sqrt{n}$).
- **Intervals** (`01_07`): percentile CI, Normal-approximation CI
  $M \pm q(\alpha/2)\,SE(M)$, coverage, one-sided intervals, prediction
  intervals.
- **Hypothesis tests** (`01_08`): invert-a-CI vs impose-the-null, null
  bootstrap (recentering shift), $p$-values, $t$-values, one-sided tests.

Part 1 is consistent and worked-example-heavy. Every formula in `01_02`–`01_08`
has a small numeric example, usually in a `callout-note`. Part 2 should match
this density. Part 1 callout style: most chapters have many `callout-note`
("Must Know") and `callout-tip` ("Test Yourself"). Notably, `01_02` and `01_03`
do **not** all have a `## Introduction` header, so the rule is applied loosely.

---

## Chapter-by-chapter notes

### 02_00 Bivariate Data (part intro)

- 3-line part intro. Adequate but thin; lists the topics. Low priority (the
  task scope is the 9 chapters; the part intro is borderline). Leave unless
  time permits.

### 02_10 Bivariate Distributions

- **Concepts/terms**: *frequency table*, *joint distribution* $\hat{p}_{xy}$,
  *marginal distributions* $\hat{p}_x$, *conditional* distributions
  $\hat{p}_{y\mid x}$, *scatterplots*, *Simpson's Paradox*.
- **Datasets/functions**: `USArrests`; `Ecdat::Wages1`; `UCBAdmissions`;
  `mvtnorm::rmvnorm`. `table`, `addmargins`, `margin.table`, `prop.table`,
  `layout`, `barplot`, `hist`, `ecdf`, `cut`, `boxplot`.
- **Notation**: $\hat{p}_{xy}$, $\hat{p}_x$, $\hat{p}_{y\mid x}$,
  $\hat{M}_X$, $\mathbf{1}(\cdot)$, $n$.
- **Strong**: the 13-student joint/marginal/conditional worked examples are
  excellent — done by hand *and* by computer. Has `## Introduction`. Good
  Simpson's-paradox 2×2 admissions table.
- **Weak / gaps**:
  - **No `callout-note` at all.** 3 callouts, all `callout-tip`. The discrete
    worked examples are first-rate but sit in body text, not in "Must Know"
    callouts.
  - **Missing the "most-stolen car" base-rate fallacy example** (explicitly
    requested in ToDo). The base-rate idea (high count ≠ high probability) is
    not in the chapter.
  - The continuous Simpson's-paradox figure (line ~377, `echo=F`) plots three
    groups but never shows the within-group vs pooled relationship — no
    regression lines, no explanation. Incomplete.
  - Marginal-mean formula $\hat{M}_X=\sum_x x\hat p_x$ has a numeric example
    (12.9). Good.
  - Commented-out interactive scatter (lines ~317–322): dead code.
- **Callouts**: 3, all tip. Need ≥1 `callout-note`.

### 02_11 Comparing Two Groups

- **Concepts/terms**: *conditional mean* $\hat{M}_{Y\mid X}$, *mean
  differences* $\hat{D}$, bootstrap CI, permutation/null distribution,
  *quantile differences*, *quantile-quantile plot*, *Kolmogorov-Smirnov
  statistic* $\hat{KS}$, *Cramer-von Mises statistic* $\hat{CVM}$.
- **Datasets/functions**: hand-built 3×2 table; `Ecdat::Wages1`;
  `twosamples`; `wooldridge::countymurders`; `mtcars`. `ecdf`, `quantile`,
  `sample`, `boxplot`.
- **Notation**: $\hat{M}_{y\mid x}$, $\hat{D}$, $\hat{KS}$, $\hat{CVM}$,
  $\hat{F}_1$, $\hat{F}_2$, $Q_1$, $Q_2$.
- **Strong**: resampling-types table is excellent. Good QQ-plot + CVM worked
  callout (Group A/B summer earnings).
- **Weak / gaps**:
  - **`twosamples` dependency** (explicit ToDo: remove it). Used 5×:
    `ks_stat`, `cvm_stat`, `ks_test`, `cvm_test`. The chapter already computes
    `which.max(abs(F2-F1))` by hand, so the statistics are easy to do in base
    R; the *tests* need a permutation loop (which the book already teaches —
    pedagogically better than a black box).
  - **No `## Introduction`.** Chapter opens straight into `## Discrete Data`.
  - Code comment mislabel: the permutation block (line ~168) is commented
    `# Null Bootstrap Distribution` but uses `replace=F` (a permutation; the
    variable is `permute_diff` and the title says "Permuted").
  - "Permutation test" is used here but only formally defined in `02_12`.
  - Several `eqnarray*` (starred) — notation guide says use `eqnarray`.
  - `boot_quant` callout: observed `d` is commented out, so `abline(v=0)` is
    the only reference line — fine, but the observed difference is never drawn.
- **Callouts**: 7 (4 note, 3 tip). Good count.

### 02_12 Statistics of Association

- **Concepts/terms**: *covariance* $\hat{C}_{XY}$, *correlation* $\hat{R}_{XY}$,
  hypothesis tests (bootstrap, permutation, null bootstrap), *Codeviance*
  $\tilde{C}_{XY}$, *median correlation* $\tilde{R}_{XY}$, *Kendall's rank
  correlation* $\hat{KT}$, *contingency table*, *Cramer's V* $\hat{CV}$,
  *chi-squared* $\hat{\chi}^2$; causation-without-correlation,
  correlation-without-causation.
- **Datasets/functions**: small 3-point set; `USArrests`; simulated.
- **Notation**: $\hat{C}_{XY}$, $\hat{R}_{XY}$, $\tilde{C}_{XY}$,
  $\tilde{R}_{XY}$, $\hat{KT}$, $\hat{\chi}^2$, $\hat{CV}$, $\hat{O}_{kj}$,
  $\hat{E}_{kj}$, $\hat{RF}_k$, $\hat{CF}_j$.
- **Strong**: the Pearson correlation 5-step worked example (math + computer)
  is excellent. The causation examples (nonlinear, heterogeneous, shared
  denominator, selection) are vivid.
- **Weak / gaps**:
  - **No `## Introduction` header** (intro prose exists at line ~5 but
    unlabeled).
  - **Notation bug**: line ~341 writes $\hat{RF}_i = \sum_j \hat O_{kj}$ —
    should be $\hat{RF}_k$ (the `_i` is wrong; per notation guide variable
    index is `_k`).
  - **Notation bug**: Cramer's V text (line ~345) says "Recalling that $I$ is
    the number of categories for $\hat X$" but the chapter defined that count
    as $K$ everywhere else. $I$ is never introduced. Should be $K$.
  - **Missing numerical examples**: Codeviance, Kendall's $\hat{KT}$,
    chi-square, and Cramer's V each have a formula and code but no by-hand
    numeric example. Pearson has a great one; the other three statistics do
    not.
  - Grammar: line ~492 "the above examples below" (above/below clash).
- **Callouts**: 6 (3 note, 3 tip). Good count, but the worked numeric examples
  are concentrated on Pearson only.

### 02_13 Simple Regression

- **Concepts/terms**: *model*, *coefficients*, *residual* $e_i$, *objective*
  (least squares), *optimal coefficients*, *slope* $b_1$, *intercept* $b_0$,
  fitted values $\hat{y}_i$, predictions, *goodness of fit*, *R-squared*
  $\hat{R}^2_{yY}$, *coefficient of determination*, TSS/ESS/RSS, bootstrap,
  jackknife SE, Normal approximation, hypothesis tests, $t$-stat, *p-value*,
  *Anscombe's Quartet*.
- **Datasets/functions**: `USArrests`; small sets {(1,2),(2,2.5),(3,4)} and
  the exercise set; `Ecdat::Wages1`; `mtcars`; `anscombe`. `lm`, `coef`,
  `predict`, `resid`, `cov`, `var`, plotly.
- **Notation**: $b_0,b_1,\hat b_0,\hat b_1,e_i,\hat e_i,\hat y_i,
  \hat C_{XY},\hat V_X,\hat R_{yY}^2,\hat{TSS},\hat{ESS},\hat{RSS},\hat t,
  s_{\hat b}$.
- **Strong**: the {(1,2),(2,2.5),(3,4)} worked example is superb — 5 steps for
  coefficients (callout-note) and 5 steps for $R^2$. Has `## Introduction`.
- **Task items (ToDo focus)**:
  - by-hand regression-coefficient calc as `callout-note` — **already done**
    (line ~106).
  - by-hand $R^2$ calc as `callout-note` — currently a **`callout-tip`** (line
    ~265). Task wants `callout-note`. Convert.
  - present the $p$-value as a `callout-tip` — currently the $p$-value
    computation (lines ~542–552) is plain body text, **not in a callout**. Add
    a `callout-tip`.
- **Weak / gaps / bugs**:
  - Line 1–3: blank line between `# Simple Regression` and `***` (other
    chapters have no blank line). Cosmetic.
  - **Bug** in coefficient callout Step 5 (line ~165): titled "design point
    $x=2.5$" but the displayed equation reads $\hat y(2)$ while computing
    $5/6+2.5$. Label should be $\hat y(2.5)$.
  - **Bug** in callout Step 2 (line ~131): $\hat V_X=\sum(X_i-\hat M_X)^2$ is
    missing the `/n` divisor in the displayed formula though the computation
    `[1+1]/3` is right. The covariance line just above *does* divide by 3.
  - $\hat R^2_{yY}$ vs $\hat R^2$ — exercises use $\hat R^2$, body uses
    $\hat R^2_{yY}$. Explained in text, mild inconsistency.
  - Broken citation `\parencite[p.92]{camerontrivedi2005}` (key not in
    `references.bib`; see cross-chapter notes).
- **Callouts**: 5 (4 note, 1 tip).

### 02_14 Local Regression

- **Concepts/terms**: local averages, *regressogram* (NOT italicized on first
  use), bins, half-width $h$, dummy $\hat{D}_i(x,h)$, *segmented/piecewise
  regression*, weighted regression, uniform kernel $k_U$, locally constant
  regression, *moving average*, naive kernel regression, bias, *local linear
  regression* (LLLS).
- **Datasets/functions**: `Ecdat::Wages1` (wage~school), `USArrests`.
  `lm`, `cut`, `split`, `predict`, `dunif`, weighted `lm`.
- **Notation**: $m(x)$, $\hat m$, $\hat D_i(x,h)$, $b_0(x,h)$,
  $\hat b_0(x,h)$, $n(x,h)$, $\hat M_Y(x,h)$, $k_U$, $w_i(x,h)$, $h$, $L$.
- **Strong**: the wage~school running example is used in most sections. The
  algebra connecting regressogram → weighted LS → locally constant regression
  is careful. 9 callouts.
- **Task items (ToDo focus)**:
  - "carry one wage-education example through the whole chapter" — **mostly
    done**; the `USArrests` Test-Yourself callouts can stay as practice.
  - "cover MSE, MAPE, and the bias-variance tradeoff" — **NOT covered.** No MSE
    or MAPE anywhere; the `#### Bias` subsection is only ~5 lines; the
    bias-variance tradeoff lives entirely in `02_15`. This is the main gap.
- **Weak / gaps / bugs**:
  - **No `## Introduction`.** Opens on `## Local Averages`.
  - *regressogram* not italicized at first use (line ~45).
  - **Bug** in the two-bin Must-Know (line ~117): the model writes
    $\mathbf{1}(\text{Educ}_i\in(0,9])$ then
    $\mathbf{1}(\text{Age}_i\in(9,18])$ — "Age" should be "Educ"
    (the example is wage on schooling, not age).
  - Local linear section says deriving $\hat b_0(x,h),\hat b_1(x,h)$ "is left
    as a homework exercise" but the `## Exercises` list does not include it.
  - `#### Bias` subsection is very thin.
- **Callouts**: 9 (4 note, 5 tip). Good count.

### 02_15 Inference

- **Concepts/terms**: *gradients*, *loess* (adaptive bandwidth), *confidence
  bands*, finite-difference gradient, marginal effect at the mean, mean of the
  gradients, hypothesis testing for gradients, sampling distributions, *bias*,
  *variance*, *bias-variance tradeoff*, *consistency*.
- **Datasets/functions**: `Ecdat::Wages1`, `USArrests`, simulated `dat_sim`.
  `loess`, `predict`, `polygon`, `matplot`, `replicate`, `kable`.
- **Strong**: the theory section (sampling distributions, bias, variance,
  consistency) with calibrated simulations is genuinely good.
- **Weak / gaps**:
  - **Thinnest-but-one Part 2 chapter** (1720 words; ToDo flags it). Only
    **3 callouts** (2 note, 1 tip) — ToDo says "2 callouts"; needs more.
  - **No `## Introduction`** (intro prose at line ~5 unlabeled).
  - Only 2 content `##` sections (Applied Methods, Theory). Structurally thin.
  - Typo line ~194: "Ee can compute".
  - **Missing numeric examples**: finite-difference gradient formula
    $\hat b_1(x)=[\hat y(x+d/2)-\hat y(x-d/2)]/d$; the "marginal effect at the
    mean" and "mean of the gradients" definitions; the consistency bandwidth
    conditions $h_n\to0,\ nh_n\to\infty$.
  - Footnote citations `@Chaudhuri1999`, `@HendersonEtAl2012` — keys not in
    `references.bib` (broken).
- **Callouts**: 3. Need 5+.

### 02_16 Bivariate Probability

- **Concepts/terms**: *random vector*, joint/marginal/conditional theoretical
  distributions, independence, law of total probability, coin-flip examples,
  *bivariate normal*, *conditional expectation* $\mathbb{E}[Y_i\mid X_i=x]$,
  covariance $\mathbb{C}$, correlation, regression coefficient.
- **Datasets/functions**: simulated coin flips, `mvtnorm::rmvnorm`, hand
  probability tables.
- **Notation**: $Prob(\cdot)$, $F(x,y)$, $F_X$, $F_Y$,
  $\mathbb{E}[Y_i\mid X_i=x]$, $\mathbb{C}[X_i,Y_i]$, $\mathbb{V}$,
  $\mu_X$, $\mu_Y$, $\rho$.
- **Strong**: the 3×3 conditional-expectation worked example and the
  cell-by-cell covariance table are excellent.
- **Weak / gaps / bugs**:
  - **No `## Introduction`.**
  - **Typo** line ~431: "We can not compute the often-used the Pearson
    correlation" — should read "We can **now** compute the often-used Pearson
    correlation" (negation flips the meaning; doubled "the").
  - **Broken code** line ~275 (`eval=F` block): `plot(XYiid, xlab=` then a
    newline — `xlab=` has no argument. Harmless because `eval=F`, but wrong.
  - Confusing line ~138: joint formula uses $\mathbf{1}(x=y)$ but the text
    then explains "$\mathbf{1}(X_i=1)$ means …" — mismatched indicator.
  - **`#### Regression Coefficient` is a stub** (lines ~507–512): just the
    formula $\mathbb{C}[X_i,Y_i]/\mathbb{V}[X_i]$, no example, no code, no
    link to `02_13`. Covariance/correlation each get full worked examples;
    this does not.
  - Subsection headers `#### **Correlation** {-}` and
    `#### **Regression Coefficient** {-}` are missing the period before `{-}`
    (style guide: `#### **Name**. {-}`).
- **Callouts**: 5 (3 note, 2 tip). Good count.

### 02_17 Testing Theory (file: StatisticalTheory)

- **Concepts/terms**: theoretical $t$-statistic, *Welch's t*, differences in
  means/medians, boxplot notches, Mann-Whitney U, regression-slope $t$-test,
  *Type I/II Error*, *significance level* $\alpha$, *power* $1-\beta$, Bayes'
  theorem, *prior/likelihood/posterior*, Bayesian screening, *sensitivity*,
  *false positive rate*, *prevalence*.
- **Datasets/functions**: simulated `rnorm`, `USArrests`, `Ecdat::Wages1`.
  `t.test`, `boxplot`, `lm`, `summary`, `replicate`, `pt`, `pnorm`.
- **Strong**: substantial chapter (was a Tier-2 expand target — already
  expanded to 481 lines). Good Type I/II table and courtroom analogy. Bayes
  worked examples (fair coins, unfair coins, screening). The "regression slope
  as a screening test" framing is a nice unifying idea.
- **Weak / gaps**:
  - **No `## Introduction`.**
  - Section header `## Type II Errors` actually covers both Type I and II.
  - Welch-Satterthwaite df formula given but no by-hand numeric example.
  - Generally in good shape; lowest-priority Part 2 chapter for content depth.
- **Callouts**: 5 (3 note, 2 tip).

### 02_18 Data Analysis

- **Concepts/terms**: interactive figures (plotly), interactive tables
  (reactable), *data-ink ratio*, static publishing, Quarto reports.
- **Datasets/functions**: `USArrests`. `plotly`, `reactable`, `stargazer`,
  `pdf`, `knitr::include_graphics`.
- **Strong**: practical, hands-on. The data-ink-ratio `callout-note` is good.
- **Weak / gaps**:
  - **Thinnest Part 2 chapter** (1342 words, 337 lines; ToDo flags 0
    callouts — actually 1 now, the data-ink callout).
  - **No `## Introduction`.**
  - Mostly prose + code with little worked-example structure. Needs more
    callouts: a "Test Yourself" on polishing a figure, and ideally a "Must
    Know" worked example (e.g., reading a summary table, or a polish
    before/after).
  - No math (expected for a viz chapter), so the "numeric example per formula"
    rule mostly does not bite — only the data-ink ratio formula, already
    illustrated qualitatively.
  - Feels like a grab-bag; transitions between Outputs subsections are abrupt.
- **Callouts**: 1 (note). Need 3+.

---

## Cross-chapter issues

1. **Missing `## Introduction` headers.** Only `02_10` and `02_13` have one.
   `02_12` and `02_15` have intro prose that is simply not under a header;
   `02_11`, `02_14`, `02_16`, `02_17`, `02_18` open directly on a content
   section. The chapter-structure guide says every chapter should have
   `## Introduction`. Adding one does not reorder existing sections. Medium
   priority; keep each intro short and genuinely orienting.

2. **Broken citations.** `references.bib` contains only `knuth84`.
   `02_13` uses `\parencite[p.92]{camerontrivedi2005}` and `02_15` uses
   `@Chaudhuri1999; @HendersonEtAl2012`. These render as unresolved
   references. `references.bib` is **outside the editable file list**, so the
   fix must be inside the `.qmd` files: convert the broken cites to plain-text
   author–year references. Low/medium priority.

3. **Notation.**
   - `02_12`: $\hat{RF}_i$ should be $\hat{RF}_k$; $I$ should be $K$ (two
     genuine bugs).
   - `eqnarray*` (starred) appears in `02_11`; the notation guide specifies
     `eqnarray`. Low priority — renders fine; note only.
   - `$h$` as bandwidth half-width is used consistently in `02_14` and matches
     `01_02`. `02_15` uses `span` for loess, which is the genuine `loess()`
     argument, not a clash. Bandwidth notation is essentially fine.
   - $\hat{R}$ is overloaded (correlation $\hat R_{XY}$ vs $R^2$
     $\hat R^2_{yY}$) but disambiguated by sub/superscripts. Do not rename.

4. **Terms used before defined.** "Permutation test" is used in `02_11`
   (impose-the-null section and exercise 1) but formally defined in `02_12`.
   A one-line parenthetical definition in `02_11` would fix this.

5. **Missed connections.**
   - `02_16` (theoretical regression coefficient) does not link back to
     `02_13` (sample regression).
   - `02_11` "conditional mean" → `02_16` "conditional expectation": no
     cross-reference between the sample and population objects.
   - `02_10`/`02_16` are sample/population mirrors of the same joint–
     marginal–conditional material; a forward/back link would help.
   - `02_14`/`02_15` already point to `03_22 Regressograms`; `02_11` points to
     `03_20`. Good.

6. **Building on Part 1.** Strong. Bootstrap/jackknife (`01_05`, `01_07`) and
   $p$-values/$t$-values (`01_08`) are reused heavily and mostly cross-linked.
   `02_10` correctly links `01_06` for marginal/univariate statistics.

7. **Numeric-example coverage** (book-wide ToDo: an example for every formula).
   Gaps: `02_12` (Codeviance, Kendall, chi-square, Cramer's V);
   `02_16` (regression coefficient); `02_15` (finite-difference gradient,
   bandwidth conditions). Elsewhere coverage is good.

8. **Callout counts.** Thin: `02_18` (1), `02_15` (3), `02_10` (3, none of
   them "Must Know"). Healthy: `02_11` (7), `02_14` (9), `02_12` (6),
   `02_16` (5), `02_17` (5), `02_13` (5).

9. **Stale freeze dirs** (`02_11_ComparingGroups`, several Part 3) exist from
   the chapter renumbering. Outside scope (not source files); noted only.
