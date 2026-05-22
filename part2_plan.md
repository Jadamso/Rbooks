# Part 2 Improvement Plan — Bivariate Data (Stats II)

Phase 2 plan, derived from `part2_analysis.md`. Organized by chapter; within
each chapter, items are ranked High → Medium → Low impact. Implementation
(Phase 3) proceeds chapter by chapter in file order, committing after each.

Guardrails: base R only, no new package dependencies, no section reordering,
no deletion of correct content, preserve existing notation/macros.

---

## 02_10 Bivariate Distributions

**High**
- *Add the "most-stolen car" base-rate fallacy worked example* (ToDo request).
  As a `callout-note` in the Conditional Distributions section: a city with
  more Civics than Other cars, where Civics are the most-stolen *count* yet
  have a *lower* theft rate. Shows $Prob(\text{model}\mid\text{stolen})$ vs
  $Prob(\text{stolen}\mid\text{model})$ — the same "change the unit of
  analysis" point the section already makes, now with a memorable example.
  *Why*: the chapter currently has zero `callout-note`s; this adds a "Must
  Know" worked example and fills an explicit ToDo gap.
- *Strengthen the continuous Simpson's-paradox figure.* Add per-group and
  pooled regression lines to the existing scatterplot and explain in prose
  what the reader sees (within-group slopes one sign, pooled slope the other).
  *Why*: currently the figure is shown with no analysis; the "overall vs
  within-group" lesson is asserted but not demonstrated.

**Medium**
- Add a short forward link from the continuous Simpson's example to
  `02_13 Simple Regression` (the lines are regressions).

**Low**
- Leave commented-out interactive-scatter hint as is (consistent with other
  chapters' optional hints).

Outcome: chapter gains ≥2 `callout-note`s, the requested base-rate example,
and a Simpson's figure that actually shows the paradox.

---

## 02_11 Comparing Two Groups

**High**
- *Remove the `twosamples` package dependency* (ToDo request). Replace:
  - `twosamples::ks_stat` → `max(abs(F1 - F2))` over pooled sorted data
    (chapter already computes `which.max(abs(F2-F1))`).
  - `twosamples::cvm_stat(power=2)` → `sum((F1 - F2)^2)`.
  - `twosamples::ks_test` / `cvm_test` → explicit permutation-test loops
    returning a statistic and a $p$-value.
  *Why*: removes the only Part 2 dependency outside the teaching set, and a
  hand-rolled permutation test reinforces the chapter's own resampling
  material rather than hiding it in a black box.

**Medium**
- *Add a `## Introduction` section* (2–4 sentences orienting the reader:
  comparing groups = analyzing a cardinal $Y$ across a factor $X$).
- *Define "permutation test" parenthetically at first use* (it is used here
  but only formally defined in `02_12`).
- Fix the mislabeled comment `# Null Bootstrap Distribution` → it is a
  permutation (`replace=F`); rename to `# Permutation Distribution`.

**Low**
- Leave `eqnarray*` as is (renders correctly; mass-editing is risky and the
  notation guide note is advisory).

Outcome: no external dependency, an Introduction, and accurate code comments.

---

## 02_12 Statistics of Association

**High**
- *Add by-hand numeric examples for Codeviance, Kendall's $\hat{KT}$, and
  Cramer's V / chi-square.* Each currently has a formula and code on
  `USArrests` but no small worked example (Pearson has an excellent 5-step
  one). Add compact worked examples (small datasets, in callouts where it
  fits the existing pattern).
  *Why*: the book-wide rule is a numeric example for every formula; three of
  four association statistics currently lack one.
- *Fix two notation bugs*: `$\hat{RF}_i$` → `$\hat{RF}_k$` in the chi-square
  definition; `$I$` → `$K$` in the Cramer's V sentence ("$I$ is the number of
  categories" — $I$ is never defined; $K$ is used everywhere else).

**Medium**
- *Add a `## Introduction` header* wrapping the existing unlabeled intro prose.

**Low**
- Grammar: "the above examples below" → "the examples above".

Outcome: every association statistic gets a numeric example; notation bugs
fixed.

---

## 02_13 Simple Regression

**High**
- *Convert the by-hand $R^2$ calculation from `callout-tip` to `callout-note`*
  (ToDo: "by-hand R-squared calculation as callout-notes"). It is a fully
  worked solution, so "Must Know" is the correct type.
- *Present the $p$-value as a `callout-tip`* (ToDo). Add a "Test Yourself"
  callout in the Impose-the-Null section that works a $p$-value with a
  concrete number and interprets it.
- *Fix bug in coefficient callout Step 5*: equation labeled $\hat{y}(2)$ but
  evaluates at $2.5$ — relabel $\hat{y}(2.5)$.
- *Fix bug in coefficient callout Step 2*: $\hat{V}_X$ display formula is
  missing the `/n` divisor (computation `[1+1]/3` is correct).

**Medium**
- Remove the stray blank line between `# Simple Regression` and `***` (every
  other chapter has them adjacent).
- Replace the broken `\parencite[p.92]{camerontrivedi2005}` (key absent from
  `references.bib`, renders as nothing in HTML) with plain text
  "(Cameron and Trivedi 2005, p. 92)".

**Low**
- Minor wording polish in the "Association is not Causation" section.

Outcome: the three ToDo callout items resolved, two math bugs fixed.

---

## 02_14 Local Regression

**High**
- *Add MSE, MAPE, and a bias-variance-tradeoff introduction* (ToDo request).
  New `## Model Fit` section before `## Exercises`: define
  $\hat{MSE}=\tfrac{1}{n}\sum\hat e_i^2$ and
  $\hat{MAPE}=\tfrac{100}{n}\sum|\hat e_i/\hat Y_i|$ with numeric values on
  the running wage~school example; then a subsection introducing the
  bias-variance tradeoff with the regressogram bin count as the concrete
  lever (few bins → high bias/low variance; many bins → low bias/high
  variance), pointing forward to `02_15` for the simulation treatment.
  *Why*: the ToDo explicitly asks for this content; it is currently absent
  and the chapter never gives the reader a way to *compare* its models.
- *Fix bug in the two-bin Must-Know*: indicator written
  $\mathbf{1}(\text{Age}_i\in(9,18])$ should be $\text{Educ}_i$ (the example
  regresses wage on schooling, not age).

**Medium**
- *Add a `## Introduction` section.*
- Italicize *regressogram* at first use.
- Resolve the "left as a homework exercise" promise for the LLLS derivation:
  add it as a fourth exercise (or soften the wording).

**Low**
- Minor wording polish around the kernel-weight discussion.

Outcome: chapter covers model fit and the tradeoff; the running example is
explicitly carried into a comparison; one bug fixed.

---

## 02_15 Inference

**High**
- *Add callouts and worked examples* (ToDo: one of the two thinnest Part 2
  chapters, only 3 callouts). Add:
  - a `callout-note` working a finite-difference gradient on small numbers;
  - a `callout-tip` contrasting "marginal effect at the mean" with "mean of
    the gradients" on a concrete tiny example;
  - a `callout-note` or `callout-tip` reinforcing the consistency idea.
- *Add numeric examples* for the finite-difference gradient formula and the
  gradient summary statistics (mean/SD of gradients).

**Medium**
- *Add a `## Introduction` section* wrapping the existing unlabeled prose.
- Fix typo "Ee can compute" → "We can compute".

**Low**
- Broken footnote citations `@Chaudhuri1999`, `@HendersonEtAl2012`: leave the
  prose, drop the unresolved `[@...]` markers or convert to plain text
  (handle conservatively — do not invent bibliographic detail).

Outcome: 5+ callouts, numeric examples for the gradient formulas, an
Introduction.

---

## 02_16 Bivariate Probability

**High**
- *Expand the `#### Regression Coefficient` stub.* It is currently one
  formula with no example. Add a numeric example using the chapter's existing
  3×3 $P_{xy}$ table ($\mathbb{C}[X_i,Y_i]/\mathbb{V}[X_i]$, reusing the
  already-computed $\mathbb{C}=0.7$ and $\mathbb{V}_X=0.49$), add code, and
  link to `02_13` for the sample analogue.
- *Fix typo* "We can not compute the often-used the Pearson correlation" →
  "We can now compute the often-used Pearson correlation" (the negation
  inverts the intended meaning; also a doubled "the").

**Medium**
- *Add a `## Introduction` section.*
- Fix broken code in the `eval=F` block: `plot(XYiid, xlab=` has a dangling
  `xlab=` with no argument.
- Fix subsection headers `#### **Correlation** {-}` and
  `#### **Regression Coefficient** {-}` to include the period:
  `#### **Correlation**. {-}`.
- Clarify the $\mathbf{1}(x=y)$ vs $\mathbf{1}(X_i=1)$ mismatch in the
  Completely-Unfair-coin example.

**Low**
- Minor wording polish.

Outcome: regression coefficient gets a worked example and a cross-link;
typos and broken code fixed.

---

## 02_17 Testing Theory

**Medium**
- *Add a `## Introduction` section.*
- Add a small by-hand numeric example for the Welch-Satterthwaite degrees of
  freedom (the formula is given but never illustrated with numbers).

**Low**
- Minor wording polish.

Outcome: the chapter is already in good shape; light additions only.

---

## 02_18 Data Analysis

**High**
- *Add callouts and worked examples* (ToDo: thinnest Part 2 chapter, ~1
  callout). Add:
  - a `callout-tip` "Test Yourself" on polishing a figure (add one necessary
    element, remove one unnecessary one);
  - a `callout-note` worked example — a compact polished interactive
    scatterplot, or a walk-through of building the summary table.

**Medium**
- *Add a `## Introduction` section.*
- Smooth the abrupt transitions between the Outputs subsections (interactive
  figures → tables → polishing).

**Low**
- Minor wording polish.

Outcome: 3+ callouts, at least one worked example, an Introduction.

---

## Cross-chapter (apply during the per-chapter passes)

- **Introductions**: add `## Introduction` to `02_11`, `02_12`, `02_14`,
  `02_15`, `02_16`, `02_17`, `02_18` (medium priority within each chapter
  above). Keep each to 2–4 orienting sentences.
- **Cross-references**: add `02_16` → `02_13` (theoretical vs sample
  regression coefficient); `02_11` conditional mean ↔ `02_16` conditional
  expectation; `02_14` → `02_15` (bias-variance simulation). Use the
  `https://jadamso.github.io/Rbooks/CHAPTER.html#section` form.
- **Notation**: do not rename anything; only fix the genuine bugs noted in
  `02_12` ($\hat{RF}_i$, $I$). Leave `eqnarray*` and the $\hat{R}$ overload.
- **Exercises**: all 9 chapters already have 3 exercises in the
  conceptual/computational/R pattern. Improve in place where a change to the
  chapter affects an exercise (e.g., `02_14` LLLS derivation as a 4th
  exercise). Do not churn working exercises.

## Priorities (overall order of effort)

1. `02_11` twosamples removal — highest-risk code change, explicit ToDo.
2. `02_13` callout/bug fixes — explicit ToDo, small and high-value.
3. `02_14` MSE/MAPE/bias-variance — explicit ToDo, new content.
4. `02_10` base-rate example — explicit ToDo, new content.
5. `02_15` and `02_18` — thinnest chapters, need callouts.
6. `02_16` regression-coefficient expansion + typo fixes.
7. `02_12` numeric examples + notation bugs.
8. `02_17` light polish.

## Completed

(Filled in during Phase 4.)
