# Part 3 Analysis — Multivariate Data (Econometrics)

Phase 1 reading notes for chapters 03_19–03_26. Written 2026-05-21.
No edits made during this phase.

---

## Cross-cutting observations (read first)

- **Broken bibliography.** `book/references.bib` contains exactly one entry
  (`knuth84`). Nine `@cite` keys are used in Part 3 and all fail to resolve:
  `@ArlotCelisse2010`, `@BatesEtAl2023`, `@Bergmeir2018`, `@Chaudhuri1999`,
  `@HaerdlePhilippe1992`, `@Hart1991`, `@HendersonEtAl2012`,
  `@OpsomerEtAl2001`, `@racine2019`. They render as broken `[?]` links.
  `references.bib` is outside the editable file list, and `02_15` (also
  outside the list) has the same broken keys. Resolution: convert the broken
  `@cite` keys *inside 03_22 and 03_26* to plain-text author–year citations
  (consistent with how Further Reading sections already cite with plain text +
  URLs). Flag the bib for the user.
- **Callout density.** Counts: 03_19=4, 03_20=6, 03_21=4, 03_22=3, 03_23=4,
  03_24=4, 03_25=4, 03_26=5. Target is 5+ of good quality. Most chapters need
  1–3 more, especially 03_22.
- **`## Introduction` section.** Only 03_20 and 03_25 have a formal
  `## Introduction`. The others open with prose then the first topic section.
  This is the established Part 3 state; do NOT add Introduction sections
  wholesale (would be invasive and risk inconsistency). 03_22 lacks any
  intro prose at all — add a short lead paragraph there.
- **`eval=F` blocks: 11 total.** 03_21 (5), 03_24 (2), 03_22 (1), 03_23 (1),
  03_25 (1), 03_26 (1). Status assessed per chapter below.
- **Empty content.** 03_22 has a literally empty code block (`## Local
  Regressions` section). 03_26 has an empty subsection header
  `#### **Bayesian Filtering** {-}` with no body.
- **Notation.** Part 3 follows the notation guide well (hats on sample
  quantities, `$\hat{b}_k$`, `$\hat{R}^2$`, etc.). One real inconsistency:
  03_19 mixes `$\hat{X}_{1i}$` (variable-first) and `$\hat{X}_{i1}$`
  (observation-first); the guide mandates `$\hat{X}_{ik}$`.
- **Builds on Part 2.** Part 3 assumes simple regression (02_13), local
  regression / regressograms (02_14), and inference / gradients (02_15).
  The bridge is mostly implicit. 03_19 jumps straight into the multivariate
  model without recalling the bivariate case; 03_22 duplicates 02_14 material
  without cross-linking.

---

## 03_19 — Multiple Linear Regression

**Title:** "Multiple Linear Regression". Sections: The Linear Model;
Variability Estimates and Hypothesis Tests; Coefficient Interpretation;
Exercises. (4 `##`, 4 `####`.)

**Concepts / key terms:** multiple linear model, explanatory/predictor
variables, Ordinary Least Squares, sum of squared errors, best-fit
coefficients $B^*$, goodness of fit, $\hat{R}^2$, adjusted $\hat{R}^2$,
joint tests, F-statistic, restricted vs unrestricted model, degrees of
freedom, null distribution by reshuffling, correctly vs misspecified model,
unbiased estimates, "adjusted correlations", $\hat{R}^2$ vs $\hat{\beta}$.

**Datasets / functions:** `USArrests` (Murder, Assault, UrbanPop, Rape);
simulated DGPs. `lm`, `coef`, `predict`, `summary`, `plot`, `abline`,
`runif`, `rbinom`, `rnorm`, `cbind`, `sample`, `plotly::plot_ly`.

**Notation introduced:** $\hat{Y}_i$, $\hat{X}_{ik}$, $b_k$, $B^*$, $e_i$,
$\hat{R}^2_{yY}$, $\hat{R}^2_{\text{adj.}}$, $\hat{ESS}/\hat{TSS}/\hat{RSS}$,
$\hat{F}_q$, $k_u$, $k_r$, $\beta_k$, $\epsilon_i$.

**Strengths:** Good simulation contrasting correctly-specified vs
misspecified DGP. The $\hat{R}^2$ vs $\hat{\beta}$ subsection is excellent
and well-motivated (wage-on-schooling example). Two strong "Test Yourself"
callouts with numerical plug-ins for $\hat{R}^2_{\text{adj.}}$ and $\hat{F}_K$.

**Weaknesses / gaps:**
- Subscript inconsistency: line 9 `$\hat{X}_{1i}, \hat{X}_{2i}$`
  (variable-first) vs line 11 `$\hat{X}_{i1}, \hat{X}_{i2}$`
  (observation-first). Line 87 also variable-first. Fix to `$\hat{X}_{ik}$`.
- The meaning of $K$ shifts: in "The Linear Model" $K$ = number of
  explanatory variables (slopes, intercept separate); in the F-test /
  $\hat{R}^2_{\text{adj.}}$ formulas $K$ = total parameters incl. intercept
  (the callout uses $K=3$ with df $(2,47)$ for $n=50$). Needs a clarifying
  sentence — do not rename.
- The misspecified-model simulation indexes `Coefs[i,]` for `i in 2:3` and
  labels them $\beta_2,\beta_3$, but the DGP has no linear $\beta$ — the
  point (that there is no true $\beta$) should be stated more sharply; the
  Must-Know callout asks the question but the body never answers it.
- No multivariate running example tying back to wage/education/experience
  as the task suggests; everything is `USArrests` or abstract simulation.
- Typo: plotly `yaxis` title `'Assualt Coefficient'` (line 125).
- The intro sentence uses `$\hat{Y}_{i}$` with a hat for the *outcome*
  before the model is even defined — fine, but the bivariate→multivariate
  bridge is abrupt. No cross-link to 02_13.
- The first plotly chart is titled "Joint Distribution of Coefficients
  (under the null)" but the recenter-at-0 lines are commented out, so it is
  NOT under the null. Title is misleading.

**Math without numerical example:** the OLS objective and $B^*$ solution
(no small worked example — could add a tiny 2-variable one); the general
$\hat{F}_q$ restricted/unrestricted formula (only the $\hat{R}^2$ special
case is plugged in).

**Callouts:** 4 (note, tip, tip, note). Good quality. Could add one more
(e.g. a worked F-test comparing nested models, or a definition callout for
OLS / adjusted $R^2$).

**Definitions italicized:** Yes — *Ordinary Least Squares*, *joint tests*,
*restrict*. *Adjusted* $R^2$ is not flagged on first use.

**`eval=F`:** none.

---

## 03_20 — Comparing Multiple Groups

**Title:** "Comparing Multiple Groups". Sections: Introduction; Equal Means
(ANOVA); Equal Distributions; Regression; Exercises. (5 `##`, 12 `####`.)

**Concepts / key terms:** factor variables (ordered/ordinal,
unordered/categorical), indicator variables / dummies, ANOVA, between-group
and within-group sum of squares, decomposition, grand mean, F-statistic,
permutation/bootstrap null, parametric F assumptions (independence,
normality, homoscedasticity), Kruskal-Wallis test, Mann-Whitney U /
Wilcoxon rank-sum, fixed effects, random effects, dummy variable estimator,
between estimator, within estimator, nested model comparison.

**Datasets / functions:** `USArrests` + `state.region`; small hand
datasets. `aov`, `summary`, `lm`, `anova`, `kruskal.test`, `aggregate`,
`boxplot`, `factor`, `nlevels`, `feols` (fixest), `pf`.

**Notation:** $\hat{Y}_{ig}$, $\hat{M}_g$, $\hat{M}_Y$, $n_g$, $G$,
$\hat{BSS}/\hat{WSS}/\hat{TSS}$, $\hat{F}$, $F_{G-1,n-G}$, $\hat{KW}$,
$\bar{r}_g$, $\hat{U}$, $\hat{D}_g$, $b_g$.

**Strengths:** Strong chapter. ANOVA decomposition has a full numerical
worked example (3 groups) with hand calculation AND code verification. The
nested-model F-test sequence is pedagogically excellent. Fixed-effects vs
dummy-variable equivalence well explained. 6 callouts — best-stocked
chapter.

**Weaknesses / gaps:**
- Kruskal-Wallis statistic $\hat{KW}$ and Mann-Whitney $\hat{U}$ have NO
  numerical example — these are the only formulas in the chapter without a
  plug-in. Add a small ranked example.
- Mann-Whitney hypotheses have a typo: `$H_0: Prob(Y_i > Y_j)=Prob(Y_i >
  Y_i)$` — the RHS should be `Prob(Y_j > Y_i)`; and $H_A$ writes
  `Prob(Y_i > Y_j) \neq Prob(Y_i > Y_j)` (identical both sides).
- After Kruskal-Wallis rejects, the chapter says "this test does not tell
  us which group is different" but never points to *post-hoc pairwise
  tests*. This is exactly where the task wants a link to the new multiple-
  hypothesis-testing section in 03_26. Currently no link.
- `F_fun` (line 111) references `dat` from the enclosing environment for
  `n <- nrow(dat)` instead of using its `Y`/`g` arguments — works here
  but is a latent bug if reused; worth a comment or fix.
- `B <- 5000` is defined (line 134) then never used — the loop uses
  `seq_along(F_nullboot)` with `F_nullboot` length 999. Dead variable.
- The "pairs bootstrap" comment says it resamples rows to build a null,
  but resampling rows of `(Y,g)` jointly is a *pairs* bootstrap, not a null
  imposition; it works because `g` is shuffled relative to a fixed `dat$Murder`.
  Actually it passes `Y=dat$Murder` (fixed) and `g=g_boot` (resampled) —
  this breaks the Y–g pairing, which IS a valid null. The comment "resample
  rows with replacement" undersells what makes it a *null* distribution.
  Worth one clarifying sentence.

**Math without numerical example:** $\hat{KW}$, $\hat{U}$ (see above).

**Callouts:** 6 — good. Quality solid.

**Definitions italicized:** Yes, thorough.

**`eval=F`:** none.

---

## 03_21 — Model Assessment

**Title:** "Model Assessment". Sections: Data Exploration; Model
Diagnostics; Data Transformations; Exercises. (4 `##`, 4 `####`.)

**Concepts / key terms:** data exploration, scatterplot matrix, conditional
relationships, model diagnostics, outliers, leverage, standardized
residuals, Cook's Distance, collinearity, Variance Inflation Factor,
normality of residuals, heteroskedasticity, data transformations,
log-linear / linear-log / log-log interpretation, elasticity, Box-Cox
transform, CES production function, concentrated optimization, smearing.

**Datasets / functions:** `USArrests`; simulated leverage example.
`lm`, `predict`, `plot.lm`, `psych::pairs.panels`, `plotly`, `hatvalues`,
`rstandard`, `cooks.distance`, `car::influencePlot`, `car::vif`,
`lmtest::bptest`, `qqnorm`, `qqline`, custom `bxcx`/`bxcx_inv`,
`expand.grid`, `apply`.

**Notation:** $r_i$ (standardized residual), $s_{[i]}$, $h_i$ (leverage),
$D_i$ (Cook's distance), $\hat{S}^2$, $p$, $\hat{VIF}_k$, $\hat{R}^2_k$,
$Y^{(\lambda)}$, $x^{(\rho)}$, $\lambda$, $\rho$.

**Strengths:** Rich diagnostics coverage. The Box-Cox / CES treatment is
unusually deep for an intro book and ties to micro theory nicely. Good
transformation-interpretation table with a plug-in "Test Yourself" callout.

**Weaknesses / gaps:**
- **Five `eval=F` blocks**, all in Model Diagnostics:
  1. line 111 `which.max(hatvalues(reg)); which.max(rstandard(reg))` —
     base R (stats), works. Should be `eval=T`.
  2. line 123 `which.max(cooks.distance(reg)); car::influencePlot(reg)` —
     `cooks.distance` is base; `car::influencePlot` needs `car`. Replace
     the `car` call with a base-R influence plot (residuals vs leverage,
     point size ∝ Cook's D), make `eval=T`.
  3. line 134 `car::vif(reg); sqrt(car::vif(reg)) > 2` — needs `car`. The
     VIF formula $1/(1-\hat{R}^2_k)$ is already in the text; compute it in
     base R with auxiliary `lm`s. Make `eval=T`, pedagogically better.
  4. line 142 hist + qqnorm of residuals — base R, works. Should be `eval=T`.
  5. line 157 `lmtest::bptest(reg)` — needs `lmtest`. Breusch-Pagan is a
     regression of squared residuals on $X$; implement in base R. Make
     `eval=T`.
- Typo: legend label `'many assualts'` (line 44).
- Typo: `*Heterskedasticity*` → *Heteroskedasticity*; "may also matters" →
  "may also matter" (line 156).
- "Standardized residuals" subsection (line 110) is squeezed between the
  outlier discussion and Cook's Distance with no `####` header — it floats.
  Fine to leave, but the floating definition could be a callout.
- Cook's Distance formula and VIF formula have NO numerical examples.
- The `psych` package: `pairs.panels` is used once. Style guide says use
  `::` for one-off — currently `library(psych)`. Minor.
- No callout on collinearity or heteroskedasticity despite being key
  "common mistakes" — candidates for `.callout-note`.

**Math without numerical example:** Cook's Distance $D_i$, $\hat{VIF}_k$,
standardized residual $r_i$. Box-Cox is illustrated via code.

**Callouts:** 4 (tip, note, tip, note). Need ~2 more (VIF/collinearity
worked example; a diagnostics "Test Yourself").

**Definitions italicized:** mostly — *leverage*, *Cook's Distance*,
*Variance Inflation Factor*, *Box-Cox*, *concentrated optimization*.
*Standardized residuals* italicized. *Heterskedasticity* italicized but
misspelled.

---

## 03_22 — Local Relationships (file: Regressograms)

**Title:** "Local Relationships". Sections: Regressograms; Local
Regressions; Model Selection; Hypothesis Testing; Exercises. (5 `##`,
2 `####`.) **Smallest chapter (1208 words); structurally thinnest
(2 subsections vs median 8).**

**Concepts / key terms:** multivariate regressogram, bins along each
dimension, OLS with/without interaction, grid prediction, multivariate
local regression, break points / kinks / discontinuities, Chow test,
F-test for breaks, model selection, leave-one-out cross-validation,
bandwidth matrix $\mathbf{H}$, k-fold CV, generalized CV, gradients,
finite differences, marginal effect at the mean, average marginal effect.

**Datasets / functions:** simulated `(x1,x2,y)`; `Ecdat::Wages1` (in the
`eval=F` block). `lm`, `cut`, `expand.grid`, `predict`, `plot`, custom
`add_legend`, `anova`, `split`, `sapply`, `pf`.

**Notation:** $\hat{D}_i(x,h)$, bins, $\mathbf{H}$ bandwidth matrix,
$h_k$, $\hat{\beta}_p(\mathbf{x})$, finite-difference gradient,
$\hat{y}[i]$ (leave-one-out prediction).

**Strengths:** The multivariate regressogram code (raw data → OLS grid →
regressogram grid, all with a shared color legend) is genuinely good and
visual. Concept of binning each dimension is clear.

**Weaknesses / gaps (this is the priority chapter):**
- **No intro prose.** Chapter opens straight into `## Regressograms`. Needs
  a short lead paragraph bridging from 02_14 (bivariate local regression)
  to the multivariate case.
- **`## Local Regressions` section is nearly empty:** one sentence then a
  literally empty ```{r}``` block (lines 125–127). Must be filled with a
  working multivariate local / piecewise regression example.
- **`eval=F` block (line 132):** the "Break Points" Chow-test example. Uses
  `Ecdat::Wages1` (an established dependency) and base-R `lm`/`anova`.
  `strucchange`/`segmented` lines are already commented out. This should
  be made `eval=T` after verifying the manual Chow-test arithmetic.
- Three of the five `##` sections (Local Regressions, Model Selection,
  Hypothesis Testing) are thin — mostly formulas with little code or
  numerical grounding.
- `\textit{}` / `\texttt{}` LaTeX used inline instead of markdown `*...*` /
  `` `...` `` (lines 168, 182). Inconsistent with the rest of the book.
- Broken `@cite`: `@ArlotCelisse2010`, `@BatesEtAl2023`, `@racine2019`,
  `@Chaudhuri1999`, `@HendersonEtAl2012`.
- No numerical example for the finite-difference gradient formula, the CV
  objective, or the bandwidth matrix.
- Only 3 callouts; needs more.
- No explicit cross-link to 02_14 Local Regression despite being its direct
  multivariate continuation.

**Verdict on expand-vs-fold:** **Expand.** The topic (multivariate
nonparametric regression: binning, local fits, CV bandwidth selection,
gradient summaries) is legitimate and distinct, and is the natural
multivariate sequel to 02_14. Folding into 03_21 would overload it. Phase 3
of the task also explicitly directs expansion. Plan: add intro prose, fill
the empty Local Regressions section with a worked multivariate piecewise /
local-linear example, enable the Chow-test block, add numerical examples
and 2–3 callouts, cross-link to 02_14.

**Callouts:** 3 (tip, note, tip).

**Definitions italicized:** *Leave-one-out Cross-validation* etc. — but via
mixed `*...*` and `\textit{}`.

---

## 03_23 — Observational Data

**Title:** "Observational Data". Sections: Temporal Interdependence;
Spatial Interdependence; Economic Interdependence; Exercises.
(4 `##`, 8 `####`.)

**Concepts / key terms:** temporal dependence, random walk, white noise,
cross-sectional vs time series, stationarity (mean / variance),
autocorrelation function (ACF), cross-correlation function (CCF), serial
dependence, spatial dependence, raster vs vector data, spatial
autocorrelation, Moran's I, endogeneity, reverse causality, simultaneity,
omitted variable, competitive market equilibrium, structural vs reduced
form, contamination bias.

**Datasets / functions:** Apple stock CSV (URL); `sf` North Carolina
`nc.shp`; `terra` Luxembourg elevation raster; simulated series / market
data. `plot_ly`, `acf`, `ccf`, `st_read`, `rast`, `autocor`,
`st_distance`, `st_centroid`, `image`, `outer`, `lm`, `sapply`, `lapply`.

**Notation:** $Y_t$, $ACF_Y(k)$, $CCF_{YX}(k)$, $E[Y_t]$, $V[Y_t]$,
$Y(s)$ (spatial), Moran's I, $Q_S/Q_D$, $\alpha_S,\beta_S$, $E_S,E_D$,
$P^*,Q^*$, contamination $\mathbb{E}[\hat{B}^*-\beta]$.

**Strengths:** Broad and well-illustrated (time series, spatial, economic
endogeneity in one arc). The competitive-market simulation is a highlight —
it grounds simultaneity concretely and sets up 03_24's IV material. ACF/CCF
panels across the 2×2 stationarity grid are effective.

**Weaknesses / gaps:**
- **`eval=F` block (line 45):** a coin-flip cumulative-average + barplot.
  It is dropped in mid-Temporal-Interdependence under "if often helps to
  see the marginal distribution too", but it plots `rbinom` white noise,
  not the series under discussion, and `barplot(... axes=FALSE)` then calls
  `axis()`. It is leftover scaffolding that does not fit. Either rework it
  to genuinely show the marginal distribution of a *time series* alongside
  the series, or remove it. Recommendation: rework into a small relevant
  example or remove.
- ACF and CCF formulas have no numerical example / no tiny hand example.
- Notation: $E[\cdot]$, $V[\cdot]$, $Cov(\cdot)$, $Var(\cdot)$ written
  without blackboard bold in the ACF/CCF/stationarity formulas; notation
  guide prefers `$\mathbb{E}[\cdot]$`, `$\mathbb{V}[\cdot]$`,
  `$\mathbb{C}[\cdot]$`. (Pre-existing; light touch — fixing improves
  consistency but is not in scope-critical. Note only.)
- "AFC" typo for "ACF" (line 130).
- Typos: "if often helps" (lines 44 & in spatial section), "intrumental"
  not here but watch 03_24.
- Random-walk shock is `runif(1,-10,10)` — fine, but the Must-Know callout
  asks to switch to `rnorm` and asks "does it change stationarity"; both
  are nonstationary, so the callout's framing could mislead. Worth a
  one-line answer hint.
- Further Reading exists (3 bullets) and is adequate; the task's "complete
  the Further Reading section" appears already addressed by a prior commit.
  Could still add one economics-journal reference for balance.
- Callout count 4; could use 1–2 more (e.g. a worked ACF on a tiny series).

**Math without numerical example:** $ACF_Y(k)$, $CCF_{YX}(k)$,
contamination bias algebra (footnote — fine as theory).

**Callouts:** 4 (note, tip, tip, note).

**Definitions italicized:** Yes, very thorough.

**`eval=F`:** 1 (line 45) — see above.

---

## 03_24 — Experimental Data

**Title:** "Experimental Data". Sections: Design Basics; Comparisons Over
Time; Quasi Experiments; Exercises. (4 `##`, 8 `####`.)

**Concepts / key terms:** control, randomization, competitive-equilibrium
experiment, comparative statics, supply shock identifying demand,
regression discontinuity (RDD) / kink (RKD), difference-in-differences
(DID), parallel trends, blocking, clustering, completely randomized design,
quasi / natural experiments, two-stage least squares (2SLS), Wald estimate,
exclusion restriction, instrument relevance, weak instruments.

**Datasets / functions:** simulated market data (carried from 03_23).
`qd_fun`, `qs_fun`, `eq_fun`, `lm`, `loess`, `predict`,
`stargazer::stargazer`, `feols` (fixest), `expand.grid`, `sapply`.

**Notation:** $\alpha_S,\beta_S,\alpha_D,\beta_D$, $dP^*/d\alpha_S$,
$dQ^*/d\alpha_S$, 2SLS equations $\hat{P},\hat{Q},\hat{p}$, $b_{1p},b_{1q}$,
Wald $B$.

**Strengths:** The single running market example threaded through RDD →
DID → 2SLS is excellent design — students see one DGP analyzed three ways.
Good caveats list on 2SLS. The comparative-statics "Test Yourself" callout
has real numerical plug-ins.

**Weaknesses / gaps:**
- **`eval=F` block #1 (line 248):** the "Within Group Variance" grid
  experiment inside `<details>`. It uses `feols`, but `library(fixest)` is
  not loaded until line 324 (later). Valuable content (shows how noise
  affects OLS vs IV). Make it work: add `library(fixest)` inside the block
  (or move the existing `library` call up) and set `eval=T`.
- **`eval=F` block #2 (line 349):** `eval=F, results='hide', echo=F` — the
  first line "We could also use a nonparametric estimator to diagnose
  linearity at each stage." is *English prose inside an R chunk* (invalid
  R), followed by commented-out code. Pure leftover scaffolding. Remove the
  chunk; if the nonparametric-diagnostic idea is worth keeping, lift the
  sentence into prose.
- `\eqref{eqn:market_supply}` etc. are LaTeX cross-references to equations
  defined in 03_23. In HTML/Quarto these likely render as broken refs
  across chapters. Worth checking; may need plain wording ("the market
  supply equation above"). Pre-existing.
- "theoretical predictions are theorefore" → "therefore" (line 60).
- "Intrumental" → "Instrumental" (line 234).
- The Blocking and Clustering subsection is very thin (3 sentences, no code,
  no example). Candidate for modest expansion — at minimum a concrete
  contrast of completely-randomized vs blocked design.
- DID and RDD subsections have good plots but no callout walking through
  *reading* the stargazer table coefficient as the estimate.
- Callout count 4; add 1–2 (e.g. a worked Wald-estimate "Test Yourself",
  or a blocking example).

**Math without numerical example:** comparative statics IS plugged in
(callout). 2SLS equations are demonstrated in code. Reasonable.

**Callouts:** 4 (tip, note, note, tip).

**Definitions italicized:** Yes — *control*, *blocking*, *quasi/natural
experiments*, *2SLS*. *Randomization* defined twice (Design Basics and
Blocking) with slightly different wording — minor.

**`eval=F`:** 2 (lines 248, 349).

---

## 03_25 — Data Scientism

**Title:** "Data Scientism". Sections: Introduction; False Positives;
Spurious Regression; Spurious Causal Impacts; Exercises. (5 `##`, 6 `####`.)

**Concepts / key terms:** spurious instruments, false discoveries, data
errors, p-hacking, multiple comparisons, spurious regression, common trends
in time series, spurious causal impacts, applying IV/RDD/DID to random
walks.

**Datasets / functions:** Tyler Vigen spurious-correlations CSV (URL);
simulated random walks. `lm`, `feols`, `summary`, `ecdf`, `plot`,
`stargazer`, `cumsum`, `runif`, `factorial`.

**Notation:** essentially none (count: 0% math) — deliberately a
discussion/demonstration chapter.

**Strengths:** Distinctive, valuable chapter. The historical-quotes opening
(Marshall, Hayek, Coase, Heckman, Deaton) is memorable. The p-hacking,
spurious-regression, and "three credible recipes on random walks"
demonstrations are compelling and the code runs.

**Weaknesses / gaps:**
- **`eval=F` block (line 161):** `results='asis', eval=F` — a fully
  commented-out stargazer of `reg1`/`reg2`. `reg1` is not defined until the
  *next* subsection. Dead scaffolding. Remove it (the following "Another
  Example" subsection already shows `summary(reg1)`).
- Sections "Introduction" and "Spurious Causal Impacts" repeat almost
  verbatim the police-wages / "find but never search for" paragraph
  (lines 6–8 vs 198–200). Redundant — tighten one.
- Typo: "OSLS" for "OLS" in a comment (line 50).
- No numerical/worked callout tying the multiple-comparisons math
  ($1-(1-\alpha)^k$) to a concrete count — the "Test Yourself" mentions it
  in prose but a small computation would land it better.
- Only 4 callouts; the chapter has lots of room for "Test Yourself"
  self-checks (e.g. predict how many tries p-hacking needs).
- The chapter never explicitly defines *multiple testing* / links forward
  to the multiple-hypothesis-testing treatment that will be added to 03_26.
  Add a cross-link.

**Math without numerical example:** $1-(1-0.001)^k$ (in a callout, prose
only — could show the computation).

**Callouts:** 4 (tip, note, tip, note).

**Definitions italicized:** *spurious instruments*, *P-hacking*. "data
errors", "spurious regression" could be flagged on first use.

**`eval=F`:** 1 (line 161).

---

## 03_26 — Misc. Multivariate Topics

**Title:** "Misc. Multivariate Topics". Sections: Prediction; Filtering;
Subsampling; Inference; Exercises. (5 `##`, 9 `####`.)

**Concepts / key terms:** describe vs explain vs predict, prediction
intervals, cross-validation (LOOCV), filtering vs smoothing, exponential
filtering, time-series cross-validation, Bayes' theorem (prior/likelihood/
posterior), subsampling (bootstrap/jackknife/random subsample), matrix
algebra in R, OLS in matrix form, unbiasedness of OLS, local linear
estimator in matrix form.

**Datasets / functions:** `USArrests`; `wooldridge::wage1`; simulated time
series. `loess`, `predict`, `lm`, `quantile`, `filter`, `npreg` (np),
`crossprod`, `tcrossprod`, `solve`, `matrix`, `sapply`, `lapply`.

**Notation:** prediction interval, $\hat{y}_{[i]}(X,h)$, $h$,
$\mathbb{E}[Y_t \mid \cdot]$, Bayes $Prob(X_i=x\mid Y_i=y)$, subsample size
$m$, matrix $\mathbf{X},\mathbf{Y},\mathbf{X}',(\mathbf{X}'\mathbf{X})^{-1}$,
$B^*$, $\beta(\mathbf{x})$, kernel matrix $\mathbf{K}(\mathbf{x})$.

**Strengths:** Bayes' theorem subsection is excellent — full numerical
example, code, and a good "Test Yourself" on prevalence. Matrix-form OLS
and the unbiasedness derivation are clean. Subsampling table (bootstrap /
jackknife / random subsample) is a nice summary.

**Weaknesses / gaps / organization:**
- **Disorganized.** "Filtering" section contains: Filtering, an EMPTY
  `#### **Bayesian Filtering** {-}` header (no body at all), then Bayes'
  Theorem. Bayes' theorem is not "filtering" — the empty header is an
  orphan. Fix: delete the empty "Bayesian Filtering" header OR give it a
  one-paragraph body that actually connects Bayes to filtering (Kalman-ish
  intuition) and then keep Bayes' Theorem as its own thing. Cleanest:
  remove the empty header; let Bayes' Theorem stand.
- **`eval=F` block (line 216):** the large TSCV block (one-sided moving
  average + LLLS, `library(np)`). It depends on `np`. The *preceding*
  block (lines 197–213) sets up `dat` but has its actual `filter()` calls
  commented out, so the section currently shows no filtering output at all.
  Decision: `np` is already used elsewhere in the book's nonparametric
  material and named in Further Reading; but enabling a 75-line block is
  risky. Preferred resolution: keep a *working, smaller* filtering example
  (the symmetric/asymmetric `filter()` moving averages, base R `stats`, no
  `np`) as `eval=T`, and either trim the TSCV block to the base-R moving-
  average TSCV (drop the `np`/LLLS half) so it runs, or remove it. Must end
  with no `eval=F`.
- **Task item — multiple hypothesis testing missing.** The chapter has no
  treatment of Bonferroni / Holm / post-hoc pairwise tests. The task
  requires adding a semi-formal section, and 03_20 must link to it.
- "## Inference" section: `#### **Matrix Calculations**` and
  `#### **Bias**` — fine, but "Inference" is a slight misnomer for what is
  really matrix-algebra + unbiasedness. Minor.
- Cross-validation appears in BOTH 03_22 (Model Selection) and 03_26
  (Prediction → Cross Validation) with near-duplicate LOOCV formulas. Not
  wrong (different framing) but worth a cross-reference instead of silent
  duplication.
- Broken `@cite`: `@OpsomerEtAl2001`, `@Hart1991`, `@HaerdlePhilippe1992`,
  `@Bergmeir2018`.
- "not that you can use" → "note that you can use" (line 405).
- The chapter is a genuine grab-bag; ordering Prediction → Filtering →
  Subsampling → Inference is roughly fine, but Subsampling sits oddly
  between Filtering and Inference. Acceptable; do not reorder per task
  constraints.

**Math without numerical example:** LOOCV objective (no plug-in); the
local-linear kernel-matrix estimator $\beta(\mathbf{x})$ (theory only).
Matrix OLS and Bayes ARE worked numerically.

**Callouts:** 5 (note, tip, tip, note, tip). Good count.

**Definitions italicized:** Yes — *describe/explain/predict*, *filtering*,
*Exponential Filtering*, *subsampling*.

**`eval=F`:** 1 (line 216).

---

## Summary table

| Ch | Words | `##`/`####` | Callouts | `eval=F` | Top issue |
|----|------:|:-----------:|:--------:|:--------:|-----------|
| 03_19 | 1606 | 4 / 4 | 4 | 0 | Subscript inconsistency; $K$ ambiguity; no wage running example |
| 03_20 | 2480 | 5 / 12 | 6 | 0 | KW / Mann-Whitney no numerical example; no link to multiple testing |
| 03_21 | 2037 | 4 / 4 | 4 | 5 | 5 `eval=F` blocks (car/lmtest → base R) |
| 03_22 | 1208 | 5 / 2 | 3 | 1 | Smallest/thinnest; empty code block; needs expansion |
| 03_23 | 2523 | 4 / 8 | 4 | 1 | `eval=F` coin-flip block is off-topic scaffolding |
| 03_24 | 2483 | 4 / 8 | 4 | 2 | `eval=F` blocks (one valuable, one broken prose-in-R) |
| 03_25 | 2586 | 5 / 6 | 4 | 1 | Dead `eval=F` stargazer; duplicated intro paragraph |
| 03_26 | 2466 | 5 / 9 | 5 | 1 | Empty "Bayesian Filtering" header; needs multiple-testing section |

**`eval=F` total: 11.** Resolution target: 0.

## Does Part 3 build logically on Part 2?

Yes, in content order (simple regression → multiple regression → local →
inference → causal designs), but the *bridges* are weak:
- 03_19 should explicitly recall 02_13's bivariate model before
  generalizing.
- 03_22 is the multivariate twin of 02_14 but never links to it.
- 03_21's diagnostics and 03_26's gradient/CV material echo 02_15 without
  cross-references.
Causal-inference concepts in 03_23–03_24 are introduced gently and remain
accessible to a student who has only had regression — the market-equilibrium
running example carries the load well. Main accessibility risk is 03_24's
cross-chapter `\eqref` to 03_23's equations.
