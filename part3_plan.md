# Part 3 Improvement Plan

Prioritized plan based on `part3_analysis.md`. Written 2026-05-21.
Items are ranked **High / Medium / Low** impact within each chapter.

Constraints honored throughout: base R only (no tidyverse, no new package
dependencies), no rewriting of working code, no section reordering, no
deletion of correct content, preserve LaTeX macros and existing notation,
edits confined to the eight `03_*` chapters.

---

## Global (applies across chapters)

- **Broken bibliography.** `references.bib` has only `knuth84`; nine `@cite`
  keys in 03_22/03_26 are unresolved. Since `references.bib` is not
  editable, convert the broken `@cite` keys *inside 03_22 and 03_26* to
  plain-text author–year citations (e.g. `(Racine, 2019)`), matching the
  plain-text style already used in Further Reading. Flag for the user in
  the final report.
- **Cross-links to Part 2.** Add `[text](https://jadamso.github.io/Rbooks/
  CHAPTER.html#section)` links where Part 3 builds on Part 2 (03_19→02_13,
  03_22→02_14, 03_21/03_26→02_15).
- **`eval=F` blocks → 0.** Resolve all 11 (complete or remove).
- **Callouts.** Bring each chapter to 5+ well-placed callouts.

---

## 03_19 — Multiple Linear Regression

**High**
- Fix subscript inconsistency: change `$\hat{X}_{1i}, \hat{X}_{2i}, \ldots$`
  (line 9) and the line-87 list to observation-first `$\hat{X}_{i1},
  \hat{X}_{i2}, \ldots$` / `$\hat{X}_{ik}$`, per the notation guide.
- Add one clarifying sentence where the F-test introduces $K$, noting that
  in the F-statistic and adjusted-$R^2$ formulas $K$ counts *all*
  parameters including the intercept (the callouts use $K=3$, df $(2,47)$).
  Do not rename the symbol.
- Fix the misleading plotly title "Joint Distribution of Coefficients
  (under the null)" — the recenter-at-null lines are commented out, so the
  plot is the ordinary (not null) joint bootstrap distribution. Either
  retitle to "Joint Bootstrap Distribution of Coefficients" or uncomment
  the recentering. Retitle (smaller change).

**Medium**
- Add a numerical/worked callout: a small two-variable nested F-test on
  `USArrests` (e.g. does adding `Rape` help?) — reinforces the F-statistic
  and complements the existing "Test Yourself" plug-ins.
- The misspecified-model simulation: add 1–2 sentences answering the
  Must-Know question (why OLS coefficients still have value as the best
  linear approximation) so the body resolves what the callout poses.
- Italicize *adjusted* $R^2$ on first use.

**Low**
- Typo: plotly `yaxis` title `'Assualt Coefficient'` → `'Assault
  Coefficient'`.
- Add a one-line bridge from 02_13 (simple regression) at the chapter
  open, with a cross-link.

## 03_20 — Comparing Multiple Groups

**High**
- Add a numerical example for the Kruskal-Wallis statistic $\hat{KW}$ and
  the Mann-Whitney $\hat{U}$ — currently the only formulas in the chapter
  with no plug-in. A small ranked dataset in a callout.
- Fix the Mann-Whitney hypotheses typo: $H_0$ RHS should be
  `Prob(Y_j > Y_i)`; $H_A$ should be
  `Prob(Y_i > Y_j) \neq Prob(Y_j > Y_i)`.
- Add a link from the Kruskal-Wallis result ("does not tell us which group
  differs") to the new Multiple Testing section in 03_26, mentioning
  post-hoc pairwise tests. Optionally a small `pairwise.t.test` / `TukeyHSD`
  callout on the region data.

**Medium**
- Remove the dead variable `B <- 5000` (line 134) — never used.
- Add one clarifying sentence to the "pairs bootstrap" callout explaining
  *why* resampling rows while passing fixed `dat$Murder` against resampled
  `g_boot` produces a null distribution (it breaks the Y–group pairing).

**Low**
- `F_fun` uses `nrow(dat)` from the enclosing scope rather than its `Y`
  argument; add a comment noting this, or compute `n <- length(Y)` inside.

## 03_21 — Model Assessment

**High**
- Resolve all five `eval=F` blocks → `eval=T`, base R only:
  1. line 111 (`hatvalues`, `rstandard` — base) → `eval=T` as-is.
  2. line 123 — keep `cooks.distance`; replace `car::influencePlot` with a
     base-R influence plot (studentized residual vs leverage, bubble size
     ∝ Cook's D).
  3. line 134 — replace `car::vif` with a base-R VIF computed from
     auxiliary regressions using the formula $\hat{VIF}_k = 1/(1-
     \hat{R}^2_k)$ already stated in the text.
  4. line 142 (residual hist + Q-Q — base) → `eval=T` as-is.
  5. line 157 — replace `lmtest::bptest` with a base-R Breusch-Pagan test
     (auxiliary regression of squared residuals on the regressors,
     statistic $n\hat{R}^2 \sim \chi^2_K$).

**Medium**
- Add a worked callout for VIF: compute it by hand for the two-regressor
  `USArrests` model and confirm against the formula.
- Add a `.callout-note` or `.callout-tip` on collinearity or
  heteroskedasticity (currently no callout in those subsections).

**Low**
- Typos: `'many assualts'` → `'many assaults'` (line 44);
  *Heterskedasticity* → *Heteroskedasticity*; "may also matters" → "may
  also matter" (line 156).
- Switch `library(psych)` to `psych::pairs.panels` (used once; style guide).

## 03_22 — Local Relationships  *(priority chapter — expand)*

**Verdict: expand, do not fold.** Multivariate nonparametric regression is
a legitimate, distinct topic and the natural sequel to 02_14.

**High**
- Add a short intro paragraph at the chapter open: bridge from bivariate
  local regression (02_14) to the multivariate case, with a cross-link.
- Fill the empty code block in `## Local Regressions` (lines 125–127) with
  a working multivariate example: a piecewise / split-sample regression
  and/or a locally-weighted fit on the simulated `(x1,x2,y)` data, plotted
  on the same prediction-grid style as the regressogram. Add explanatory
  prose.
- Resolve the `eval=F` Chow-test block (line 132) → `eval=T`. The math is
  correct (verified: `Ft` reduces to the standard Chow F). Uses
  `Ecdat::Wages1` (established dependency) and base R. Rename the inner
  local `reg` to `reg_sub` to remove variable shadowing. Keep
  `strucchange`/`segmented` lines commented as pointers.
- Expand the thin `## Model Selection` and `## Hypothesis Testing`
  sections with a worked numerical example each (e.g. compute a
  finite-difference gradient on the regressogram; a small LOOCV-over-bins
  comparison).

**Medium**
- Add 2–3 callouts: a "Must Know" worked bin-mean computation; a "Test
  Yourself" on choosing the number of bins (bias–variance); a worked
  finite-difference gradient.
- Convert inline `\textit{}` / `\texttt{}` to markdown `*...*` / `` `...` ``.
- Convert broken `@cite` keys to plain-text citations.

**Low**
- Cross-link the cross-validation discussion to 03_26 (which repeats it).

## 03_23 — Observational Data

**High**
- Resolve the `eval=F` coin-flip block (line 45). It is off-topic
  scaffolding (plots `rbinom` white noise, not the series under
  discussion). Replace it with a small, relevant `eval=T` example: show the
  marginal distribution (histogram) of an actual simulated series *beside*
  its time path — genuinely illustrating "see the marginal distribution
  too." If a clean fit is not achievable, remove the block and the
  orphaned lead sentence.

**Medium**
- Add a numerical example for the ACF: a tiny series with the lag-1
  autocorrelation computed by hand in a callout, then checked with `acf()`.
- Fix "AFC" → "ACF" (line 130).
- Add 1 economics/finance reference to Further Reading for field balance
  (the section is otherwise adequate; the task item appears already done
  by a prior commit).

**Low**
- Convert bare `E[\cdot]`, `V[\cdot]`, `Cov`, `Var` in the ACF/CCF/
  stationarity formulas to `$\mathbb{E}[\cdot]$`, `$\mathbb{V}[\cdot]$`,
  `$\mathbb{C}[\cdot]$` per the notation guide (light, consistency only).
- Add a short answer hint to the random-walk Must-Know callout (both
  `runif` and `rnorm` shocks give a nonstationary walk).

## 03_24 — Experimental Data

**High**
- Resolve `eval=F` block #1 (line 248, "Within Group Variance"): add
  `library(fixest)` inside the block (or move the existing line up) and set
  `eval=T`. Content is valuable (OLS vs IV under different noise).
- Resolve `eval=F` block #2 (line 349): remove it. It is leftover
  scaffolding — English prose sits inside an R chunk (invalid R) and the
  rest is commented out. If the nonparametric-diagnostic idea is worth
  keeping, lift the one sentence into prose above.

**Medium**
- Expand the very thin "Blocking and Clustering" subsection: a concrete
  contrast of completely-randomized vs randomized-block design, ideally a
  short code illustration or worked example.
- Add a callout that walks through reading the RDD or DID stargazer table —
  which coefficient is the estimate and how to interpret it.

**Low**
- Typos: "theorefore" → "therefore" (line 60); "Intrumental" →
  "Instrumental" (line 234).
- Note (do not necessarily fix) the cross-chapter `\eqref` to 03_23's
  equation labels; if they render broken, reword to "the supply equation in
  the previous chapter." Flag for user.

## 03_25 — Data Scientism

**High**
- Resolve the `eval=F` block (line 161): remove it. Fully commented-out
  stargazer of `reg1`/`reg2`; `reg1` is not defined until the next
  subsection, which already shows `summary(reg1)`.

**Medium**
- De-duplicate: the police-wages / "find but never search for" paragraph
  is repeated near-verbatim in `## Introduction` (lines 6–8) and
  `## Spurious Causal Impacts` (lines 198–200). Tighten the second
  occurrence to a brief callback.
- Add a "Test Yourself" callout that computes the multiple-comparisons
  probability $1-(1-\alpha)^k$ for a few $k$ in R, making the p-hacking
  point concrete.
- Add a forward cross-link to the new Multiple Testing section in 03_26.

**Low**
- Typo: "OSLS" → "OLS" (comment, line 50).

## 03_26 — Misc. Multivariate Topics

**High**
- **Add a new `## Multiple Testing` section** (before `## Exercises`) with a
  semi-formal treatment: family-wise error rate, Bonferroni and Holm
  corrections, and post-hoc pairwise tests. Use base R only —
  `pairwise.t.test`, `p.adjust` (`'bonferroni'`, `'holm'`, `'BH'`),
  `TukeyHSD` on an `aov` object. Include a worked example on the
  `USArrests` + `state.region` data so it ties back to 03_20. Add 1–2
  callouts. This is the anchor for the 03_20 and 03_25 cross-links.
- Resolve the `eval=F` TSCV block (line 216). Replace with a *working*
  base-R filtering example: uncomment and run the symmetric / asymmetric
  `filter()` moving averages already drafted above it, plot the smoothed
  series, and keep a base-R one-sided moving-average TSCV that runs. Drop
  the `np`/LLLS half (avoids the `np` dependency and a 75-line block).
  Result: no `eval=F`, a real figure where there is currently none.
- Remove the empty `#### **Bayesian Filtering** {-}` header (line 294) — it
  has no body and Bayes' theorem is not filtering. Let `#### **Bayes'
  Theorem**` stand on its own.

**Medium**
- Add a numerical plug-in for the LOOCV objective (small dataset, compute
  one leave-one-out error by hand in a callout).
- Cross-reference the cross-validation material to 03_22 instead of
  silently duplicating it.
- Convert broken `@cite` keys to plain-text citations.

**Low**
- Typo: "not that you can use" → "note that you can use" (line 405).

---

## Suggested sequencing

1. Phase 1+2 deliverables — commit `part3_analysis.md` + `part3_plan.md`.
2. 03_22 (largest single effort — expansion) and 03_26 (new section).
3. 03_21 (five `eval=F` blocks).
4. 03_19, 03_20 (link target depends on 03_26's new section existing).
5. 03_23, 03_24, 03_25 (`eval=F` + polish).
6. Phase 4 self-review.

Commit after each chapter with a concise one-line message.
