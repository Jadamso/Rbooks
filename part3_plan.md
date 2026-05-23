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

---

## Completed (2026-05-22)

### Done

**03_19** (a5ed53e)
- Notation: `\hat{X}_{1i}` → `\hat{X}_{i1}` at lines 9 and 87 (observation-first).
- Added clarifying footnote on $K$ counting all parameters including intercept.
- Retitled plotly chart to "Joint Bootstrap Distribution of Coefficients"; fixed `Assualt` → `Assault` typo (axis + hover text).
- Italicized *adjusted* $\hat{R}^2$ on first use.
- New Must-Know callout: nested F-test on `USArrests` using `anova()` (Rape → no improvement).
- Bridge sentence at chapter open with link to 02_13.
- Added prose answering Must-Know question on misspecified-model simulation.

**03_20** (87ad0cf)
- Fixed Mann-Whitney typo: $H_0$ RHS now `Prob(Y_j > Y_i)`; $H_A$ now `\neq Prob(Y_j > Y_i)`.
- New Must-Know callout: worked Kruskal-Wallis numerical example ($\hat{KW}=7.2$ on $\{1,\ldots,9\}$) and Mann-Whitney $\hat{U}=3$ on $A=\{1,3,5\}, B=\{2,4,6\}$, both checked against R.
- New Must-Know callout: post-hoc `pairwise.wilcox.test` on regional data with Holm correction.
- Cross-link from KW result to new 03_26 Multiple Testing section.
- Removed dead `B <- 5000`.
- Added intuition sentence to pairs-bootstrap callout explaining why resampling group labels breaks the Y-group pairing.
- F_fun now computes `n <- length(Y)` from its argument, not from enclosing `dat`.

**03_21** (5044f26, predecessor)
- Five `eval=F` blocks all resolved with base R (influence plot from `hatvalues`/`rstandard`/`cooks.distance`, manual VIF, manual Breusch-Pagan).
- Worked Must-Know callout for VIF; Test-Yourself callout for Breusch-Pagan/heteroskedasticity interpretation.
- Typos fixed: "many assualts", "Heterskedasticity", "may also matters".

**03_22** (8807118, predecessor)
- Filled empty `## Local Regressions` code block with a working multivariate piecewise regression (`y ~ x1c/(x1+x2)`).
- Resolved `eval=F` Chow-test block; renamed inner `reg` → `reg_sub`.
- Expanded `## Model Selection` with a 5-fold CV-over-bins example.
- Expanded `## Hypothesis Testing` with finite-difference and piecewise-slope gradient examples.
- New callouts: regressogram-cell-mean Must-Know, CV Test-Yourself, finite-difference gradient Must-Know.
- Broken `@cite` keys (Racine, Arlot/Celisse, Bates, Chaudhuri, Henderson) converted to plain-text citations.
- Bridge paragraph at chapter open linking to 02_14.

**03_23** (feee673)
- Replaced off-topic `eval=F` coin-flip block with a working time-path + marginal-distribution layout of the random walk simulated above.
- New Must-Know callout: ACF worked example $\widehat{ACF}(1)=0.4$ on $y=(2,4,6,8,10)$, checked against `acf()`.
- Fixed "AFC" → "ACF".
- Notation: bare `E`, `V`, `Cov`, `Var` in stationarity and ACF/CCF formulas → $\mathbb{E}, \mathbb{V}, \mathbb{C}$.
- Random-walk Must-Know now has a hint answering the question (`runif` vs `rnorm` shocks both give nonstationary walks).

**03_24** (fdb233a)
- Resolved `eval=F` "Within Group Variance" block: `library(fixest)` added inside the block, runs.
- Removed orphan `eval=F` block (commented-out IV scaffolding); lifted the one useful sentence into prose.
- Replaced broken cross-chapter `\eqref{eqn:market_supply}` and `\eqref{eqn:market_demand}` with plain "the supply/demand equation from the previous chapter".
- Expanded "Blocking and Clustering" with a concrete completely-randomized vs blocked assignment code example.
- New Test-Yourself callout walking through how to read the DID stargazer table (intercept, main effects, interaction).
- Typos: "theorefore" → "therefore"; "Intrumental" → "Instrumental".

**03_25** (ed5f2db)
- Removed `eval=F` fully-commented stargazer block (line 161).
- Tightened duplicate police-wages paragraph in Spurious Causal Impacts to a brief callback to the intro.
- Expanded the p-hacking Test-Yourself callout into a concrete `1-(1-α)^k` computation across $k=1,10,100,700,5000$ with a forward link to 03_26 Multiple Testing.
- Fixed "OSLS" → "OLS" comment typo.

**03_26** (7bb536c, predecessor)
- **Added new `## Multiple Testing` section** before `## Exercises` — FWER, Bonferroni and Holm via `p.adjust`, post-hoc `pairwise.t.test` and `TukeyHSD` on `USArrests` + `state.region`. Two callouts.
- Resolved `eval=F` TSCV block with a working base-R symmetric/asymmetric filter and one-sided MA TSCV; produces real figures.
- Removed empty `#### **Bayesian Filtering** {-}` header.
- Broken `@cite` keys (Racine, Hyndman/Athanasopoulos, Hansen) converted to plain-text citations.
- "not that you can use" → "note that you can use".

### Deferred (with reasons)

- **03_21 — Switch `library(psych)` to `psych::pairs.panels`.** Low-priority style refactor; the chapter's substantive work (5 `eval=F` blocks, VIF/BP callouts, typos) is done.
- **03_22 — Cross-link the cross-validation discussion to 03_26.** The reverse link (03_26 → 03_22 Model Selection) was added by my predecessor; the forward link from 03_22 was not. Low priority.
- **03_23 — Add one econ/finance Further Reading entry.** All three existing entries (Effect Book, Mostly Harmless, Mixtape) are already econ-focused, so the field-balance concern is already satisfied. No change needed.
- **03_24 — Optional: contrast completely-randomized vs randomized-block by re-fitting the supply-and-demand simulation under each.** The added code shows assignment balance but does not run a comparison estimator. Plan only asked for a "short code illustration", which is what was delivered.

### Verification

- `grep -E 'eval\s*=\s*F' book/03_*.qmd` returns no matches (0 of 11 remaining).
- `grep '@cite\|@\w+\d{4}' book/03_*.qmd` returns no matches.
- All chapter cross-links checked: `#multiple-testing` exists in 03_26 (line 468), `#matrix-calculations` exists in 03_26 (line 380), `#model-selection` exists in 03_22 (line 228).
- Each modified chapter re-read end-to-end for flow; no surviving plan items beyond Deferred above.
- 9 commits on top of main (8 chapter/section improvements + 1 planning commit).
