# Part 1 Analysis Notes (Phase 1)

This document records observations from reading all Part 1 chapters cover to cover, plus skims of Part 2 chapters (02_10, 02_13, 02_17) for style reference. It is intended only as the foundation for `part1_plan.md`.

---

## Cross-Chapter Issues

### Structural defects

* **01_06 PopStatistics has NO chapter title or `***` rule.** The file begins with `## Statistical Theory` on line 1. By the project callout style guide (`Code/callout_style_guide.md`), every chapter must start with `# Title` then `***`. This breaks the part-of-book navigation and the chapter title in the rendered HTML.
* **01_09 AdvancedProbability is missing the `***` rule.** Line 1 is `# Advanced Probability`, line 2 is blank, line 3 starts content. Needs a `***` on line 2.
* **Missing `## Introduction` sections** in: 00_01 FirstSteps, 01_02 Data, 01_05 Sampling, 01_06 PopStatistics, 01_07 Intervals, 01_08 HypothesisTests, 01_09 AdvancedProbability. The style guide requires every chapter to open with `## Introduction`. Only 01_03 and 01_04 have it.

### Broken / incomplete content

* **01_09 line 17 sentence is truncated**: *"If the coin is unfair; probability of heads equals $0.25$, then the corresponding outcomes $\{2,1,1,0\}$ have probability"* — the sentence stops mid-clause. No answer follows. This is the introductory worked example for the Binomial distribution.
* **01_05 SE worked example uses inconsistent numbers.** Prose says *"Suppose we have five bootstrap estimates of the sample mean: $\{8,5,4,7,8\}$"* but the calculation that follows uses $\{3, 5, 6, 7, 9\}$. The values $\{3, 5, 6, 7, 9\}$ are what produces the stated mean of 6 and SE of 2.
* **01_05 jackknife/bootstrap intuition callouts are mislabelled.** Two callouts titled "Must Know" actually ask the student to *do* something ("compute the jackknife estimate of the median"). These are Test Yourself prompts, not worked examples.

### Notation consistency

* `\hat{X}_i` (with hat) is used throughout 01_02–01_05 to denote a realized data value, before 01_06 formally introduces the distinction between `X_i` (random variable) and `\hat{X}_i` (realization). A reader who works through 01_02 first will not know what the hat means. The convention is consistent across chapters but introduced too late.
* Bandwidth `h` is used differently inside 01_02 itself: in the histogram section the prose says `h` is the **half-width** of a bin and bins are `(x-h, x+h]`. In the kernel-density section the inequality is `|X_i - x|/h <= 1`, i.e., `h` is the **full** bandwidth in that formulation. These match in numerical effect (the rectangular kernel of full bandwidth `h` covers the same width as the histogram half-width `h` if you allow a factor of 2), but the language clashes. The ToDo.md item "Harmonize bandwidth notations" is real.
* 01_05 mixes `\hat{M}_{-i}` (in figure axis labels) with `\hat{M}_{i}^{jack}` (in text) for jackknife leave-one-out means.
* 01_07 writes the interval as `[M - E, M + E]` in some places and as `[\hat{M} - E, \hat{M} + E]` in the worked example. The chapter switches between $M$ (estimator) and $\hat{M}$ (estimate) in formulas without flagging it. Same in 01_06.
* In 01_03, the skewness denominator is `\hat{S}^3` (sample sd cubed), but `\hat{S}` itself was defined earlier with the divide-by-n version. Worth noting that this means the chapter's skewness is the divide-by-n flavor.

### Definition italics

Italicization is broadly consistent but a few first uses are not italicized:

* 00_01: *replicable*, *reproducible*, *scalars*, *vectors*, *matrices*, *Functions* — all italicized. Good.
* 01_02: *cardinal*, *factor*, *Discrete*, *Continuous*, *Ordered*, *Unordered*, *character strings*, *Empirical Cumulative Distribution Function*, *quantiles*, *interquartile range*, *outliers*, *kernel density* — all italicized. *Boxplots* italicized. *median*, *min*, *max*, *mode* — italicized in passing in the quantiles callout. Good.
* 01_03: *mean*, *variance*, *standard deviation*, *Median*, *Interquartile Range*, *Median Absolute Deviation*, *weighted mean*, *skewness*, *Concave*, *Convex*, *power transformations*, *exponential transformation*, *logarithmic transformation*, *Box–Cox Transform*. Good.
* 01_04: *Random variables*, *sample space*, *probability*, *cumulative distribution function*, *probability mass function*, *Bernoulli*, *Discrete Uniform*, *Categorical*, *probability density function*, *Normal*, *Gaussian* — italicized. Good.
* 01_05: *sample*, *population*, *simple random sample*, *sampling distribution*, *Law of Large Numbers*, *Central Limit Theorem*, *resample*, *jackknife*, *bootstrap*, *Standard Error*, *standard error* — italicized. The *Fundamental Theorem of Statistics* is also italicized. *permutations*, *binomial coefficient* in callout — good. **But** *consistent* (estimators) appears only in a footnote, with italics — fine.
* 01_06: *estimate*, *estimator* introduced and italicized inside a long sentence — could be more prominent. *Linearity of Expectations* italicized.
* 01_07: *confidence interval*, *critical values*, *margin of error*, *coverage*, *precision*, *accuracy*, *prediction interval* — italicized. Good.
* 01_08: *hypothesis test*, *rejection region*, *null distribution*, *null hypothesis*, *$p$-value*, *$t$-value*, *two-sided test*, *one-sided tests*, *alternative hypotheses* — italicized. Good.
* 01_09: *Poisson distribution*, *de Moivre–Laplace Theorem*, *Poisson Limit Theorem*, *union*, *intersection*, *mutually exclusive*, *inclusion–exclusion*, *mutually independent*, *conditional probability*, *Bayes' theorem* — italicized. Missing italics on "Binomial distribution" (only linked), and "Beta distribution" (only linked).

### Callout title strings

The style guide says every callout title is exactly `"Must Know"` or `"Test Yourself"`. Spot-checked all chapters — every callout uses the right two strings. Two callouts in 01_03 and 01_06 use `collapse="false"` instead of `"true"`. Style guide allows that as a deliberate exception, but consistency would be cleaner.

### Forward / back references

Current cross-references:

* 01_02 → 02_10 (bivariate visualization) ✓
* 01_05 → 00_01 (loops link) ✓
* 01_06 → 01_05 (sampling distribution refresher) is missing — would be a good back-link
* 01_07 → 02_13 (regression CIs) ✓
* 01_08 → 02_11 (two-group tests) ✓
* 01_09 → 01_05 (binomial coefficient) ✓

Missing high-value cross-references:

* 01_03 should back-link to 01_02 (quantiles) when median is introduced.
* 01_03 transformations could forward-link to 03_26 (transformations) — but that chapter isn't in this part, skip.
* 01_06 should back-link to 01_05 (resampling) when bootstrap SE appears.
* 01_07 should back-link to 01_05 when bootstrap distribution is reused.
* 01_08 should back-link to 01_07 when CIs are inverted.

---

## Per-Chapter Notes

### 00_01 First Steps (459 lines)

**Concepts**: replicable vs reproducible, RStudio panes, comments, variables/assignment, scripting, scalars, vectors, matrices, custom functions, sum, apply, seq, sort, order, for loops, logical operators.

**Datasets**: USArrests (only briefly, in `## Mathematical Functions`).

**Notation**: minimal; just arithmetic and assignment.

**Strengths**:
* "Copy / Run / Predict / Change / Break / Fix" cycle is good pedagogy.
* The two demo callouts (Must Know / Test Yourself) are deliberately placed early so later chapters' callouts are not surprising.
* Common-mistakes inline comments (`X +   1` capitalization warning, `Y < - 43` spacing).

**Weaknesses / gaps**:
* No `## Introduction`. Section structure jumps to `## Why Program in R?`.
* The chapter title "First Steps" and a section title "First Steps" collide. The section should probably be `## Setup` or `## Installing R`.
* "Mathematical Functions" subsection ends abruptly. The `add_two` example doesn't demonstrate why functions are useful; could end with a worked one-line custom statistic (e.g., a sum-of-squares helper).
* `## Mathematical Objects` lacks an `## Introduction`-style framing paragraph.
* "Common Functions" has `?sum` commented out — could promote to active.
* `## Exercises` has only 3 questions; minimum per task spec. They are well-formed (conceptual + by-hand + R coding).
* No "Further Reading" issues — good list.
* Slight code-style: `(x >= 1) & (x < 2)` would be clearer as `x >= 1 & x < 2` without parens (precedence is fine), but the author's parenthesized version is more pedagogically explicit, so keep.

### 01_02 Data (564 lines)

**Concepts**: cardinal vs factor data, discrete vs continuous, ordered vs unordered, strings, lists, data.frames, arrays, proportions, empirical mass function, histogram density, kernel density, ECDF, quantiles, deciles, quartiles, boxplots.

**Datasets**: USArrests (Murder primarily), simple synthetic `{3, 3.1, 0.02}`.

**Notation**: `\hat{X}_i`, particular value `x`, `\hat{p}_x` (mass), `\hat{f}(x)` (density), `\hat{F}(x)` (ECDF), `\hat{Q}(p)` (quantile), `n`, `h` (half-width or bandwidth — see cross-chapter note).

**Strengths**:
* Worked example with `{3, 3.1, 0.02}` runs through histogram density, ECDF, and quantiles, building familiarity with the same numbers.
* Histogram → kernel-density transition is gradual and well-motivated.
* Three kernels visualized.
* Quantile tie-breaking footnote is honest about the messy small-n case.

**Weaknesses / gaps**:
* No `## Introduction`. Starts at `## Data Types`.
* `\hat{X}_i` notation introduced without explanation. The proportions section just writes "we will often work with data as vector, where there are $n$ observations and $\hat{X}_{i}$ is the value of the $i$th one". The hat looks decorative to a first-time reader.
* "Outer products yield arrays" code chunk is dangling — purpose isn't clear in the chapter narrative.
* `13 subsections` — at the high outlier (per ToDo.md analysis). Could probably consolidate Lists/Data.frames/Arrays into one "Storing Data" subsection.
* Boxplot section says "*Boxplots* also summarize the distribution" — placement is fine but boxplots come *after* quantiles (good) and could explicitly say "the box covers IQR" with a labeled diagram.
* Mode is only mentioned in passing in the quantile callout ("The number $0$ is also special: the most frequent observation is called the *mode*"). 01_03 then re-introduces it. Either define it here for real or move the parenthetical to 01_03.
* Exercise 2 is good (hand histogram on `mtcars$mpg`). Exercise 1 is conceptual. Exercise 3 is R. All meet the spec.

### 01_03 Descriptive Statistics (535 lines)

**Concepts**: statistics as functions, summary, mean, variance, sd, median, IQR, MAD, weighted statistics (mean, quantile), mode, frequency spread/concentration, skewness, kurtosis, clusters/gaps, transformations (power, exp, log, Box–Cox), Jensen's inequality.

**Datasets**: USArrests, synthetic mixtures.

**Notation**: `\hat{M}, \hat{V}, \hat{S}, \tilde{M}, \hat{V}', \hat{S}'`, `\text{MAD}`, `g(X_i)`, `\hat{M}_X, \hat{M}_Y`.

**Strengths**:
* Has `## Introduction`.
* Worked numerical example for variance (`{1, 4, 10}`).
* Generalisation of mean to weighted statistics is clean.
* Box–Cox introduced with code and three-panel plot of `λ ∈ {-1, 0, 1}`.

**Weaknesses / gaps**:
* Skewness and kurtosis: formulas given but worked examples are code-only, no by-hand calc. The dataset for the skewness example uses `X^2` and `X^3` without showing the intermediate cubed-deviation sum.
* Skewness uses `mean((X - X_mean)^3)` (divide-by-n) but `sd(X)^3` (divide-by-(n-1)). Mixed; should note or align.
* Mode subsection is short. Could use a fully worked frequency-table example (the code is there; just narrate it).
* Clusters/Gaps subsection has two `echo=F` mixture simulations and no real exposition. A reader sees a multimodal histogram and is told "remember a picture is worth a thousand words", then the section ends. This is the weakest section in the chapter — barely a section.
* Jensen's inequality definition is "Concave functions curve inwards, like the inside of a cave." Cute but very brief. Could add the formal statement `g(E[X]) >= E[g(X)]` for concave next to the picture-intuition.
* The Weighted Quantiles callout has `collapse="false"` (one of only two in Part 1) — inconsistent.
* Exercises are good: conceptual median-robustness, hand variance on `{2,5,5,8,12}`, R skewness comparison.

### 01_04 Random Variables (517 lines)

**Concepts**: random variable, sample space, probability, CDF, in/out probability rules, Bernoulli, Discrete Uniform, Multinoulli, Categorical, PMF, Continuous Uniform, Exponential, Normal, PDF, R `dXXX`/`pXXX`/`rXXX` family.

**Datasets**: synthetic.

**Notation**: `X_i` vs `\hat{X}_i`, `Prob(X_i = x)`, `F(x)`, `f(x)`, `p`, `\mu`, `\sigma`, `\lambda`.

**Strengths**:
* Has `## Introduction`.
* Carefully distinguishes the unflipped coin (random variable) from the flipped coin (realization).
* Cumulative-proportion plot at the top is a good visual hook for LLN-like behavior even before LLN is named.
* The "K-sided die" Must Know callout walks through CDF in/out probabilities concretely.

**Weaknesses / gaps**:
* The Bernoulli mathematical example only states the formula; the actual `c(0,1)` with probabilities `c(3/4, 1/4)` does not show by-hand calculation of `E[X_i] = p`. (01_06 does this calculation, but a numerical preview here would help.)
* "Probability Rules" subsection (in/out probabilities) has dense formulas but no worked example. The K-sided-die callout that follows it covers these implicitly but does not cite the rules.
* The Exponential `dXXX/pXXX/rXXX` table is good but the Exponential parameter is called "shape" parameter `λ > 0`. It is really the *rate* parameter (mean = `1/λ`). 01_06 later writes `mean = 1/λ` correctly. Should explicitly say "rate".
* The Normal PDF formula is presented; could be followed by a one-line "this is a bell shape centered at μ with spread σ" instead of jumping to code.
* Multinoulli random-letters example with 26 levels is overlong for the educational point being made.
* The flight Calgary→Kamloops callout has no answer/code — purely a prompt. That's intentional but the layout might mislead a first reader.

### 01_05 Sampling (780 lines — largest in Part 1)

**Concepts**: simple random sample (with/without replacement), permutations, binomial coefficient, infinite population intuition, sampling distribution, LLN, CLT, Fundamental Theorem of Statistics / Glivenko–Cantelli, jackknife, bootstrap, comparison of the two, standard error vs standard deviation, diminishing-returns SE curve, generalization to other statistics, inverse sampling (empirical and theoretical).

**Datasets**: USArrests (Murder), simulated uniform/Hesterberg mixture.

**Notation**: `\hat{M}_b^{boot}, \bar{\hat{M}}^{boot}, \hat{SE}^{boot}, \hat{M}_i^{jack}, \hat{SE}^{jack}`, `B`, `n`.

**Strengths**:
* The Hesterberg-style figure linking sample → resamples → resampling distribution is a strong centerpiece.
* The "Sampling Distribution" worked example on `{18,20,22,24}` student ages is a great first concrete demonstration.
* Clearly distinguishes `sd` (within sample) from SE (across samples).
* Explicit small-B worked example for bootstrap SE: `{3,5,6,7,9}` → mean 6, SE 2.
* Discusses diminishing returns of more data.

**Weaknesses / gaps**:
* No `## Introduction` (starts with `## Sampling`).
* **Bug**: SE worked example text says `{8,5,4,7,8}` but uses `{3,5,6,7,9}` in the calculation. This must be fixed.
* Two Must-Know callouts (Jackknife and Bootstrap) actually ask the student to compute — Test-Yourself style, mislabelled.
* The "Drawing Samples" section at the end (inverse sampling via Dagum) is fairly advanced and feels disconnected. It's a niche aside; could be moved to 01_09 or marked optional.
* The Cauchy / "fat tails" Test Yourself code chunk is `eval=F` — students see code but no plot. Either turn on or remove.
* Jackknife SE formula appears with a square-root-of-n correction that is explained, but the explanation could be tighter ("their spread is therefore of order 1/n smaller…").
* No back-link to 01_03 when "median" reappears.

### 01_06 PopStatistics (443 lines)

**Concepts**: population vs sample, estimate vs estimator vs population parameter, expected value (discrete), variance/sd (discrete), LOTUS, expectation/variance for continuous (in collapsed Advanced block), estimating probabilities with data, estimating means/variances with probability weights, linearity of expectation, SE of the mean from `σ/√n`, normal approximation for sampling distribution.

**Datasets**: USArrests, synthetic dice/coins.

**Notation**: `μ, σ, σ^2, M, V, \mathbb{E}, \mathbb{V}, \hat{p}_x, M_X, V_X, S, \hat{S}, SE(M)`.

**Strengths**:
* The estimate / estimator / population-parameter table is the clearest treatment in the book.
* Worked five-sided-die expected value and variance.
* The unfair coin (p = 3/4) numerical example for `E[X]` and `V[X]`.
* LOTUS introduction with concrete `g(x) = x^2 + 1`.

**Weaknesses / gaps**:
* **Missing `# Title` and `***`.** The file starts with `## Statistical Theory`. This is the single most impactful fix in Part 1.
* No `## Introduction` (would need to be created alongside the title).
* The "Advanced and Optional" collapsed block for continuous RV integration is correct but the chapter currently has no "stay-on-the-surface" worked example for continuous `E[X]`. The Exponential `E[X] = 1/λ` claim at the start of "Continuous Random Variables" is just asserted without working through any integral or showing a simulation that converges to the stated mean.
* "Linearity of Expectations" worked example (the Bernoulli sum) is correct but visually dense — many `[1+1][p × p]` brackets.
* The chapter ends with a Bootstrap-vs-Normal-approximation plot but no clear closing transition into the next chapter (intervals).
* Lacks a reference back to 01_05 for the bootstrap loop.

### 01_07 Intervals (400 lines)

**Concepts**: critical value, percentile CI from bootstrap, normal-approximation CI, margin of error, coverage, sampling-distribution quantile CI, interval size & precision–accuracy tradeoff, one-sided intervals, prediction intervals.

**Datasets**: USArrests, simulated uniform.

**Notation**: `M ± q(α/2) · SE(M)`, `E` (margin of error), `1−α`, `\hat{M}, \hat{S}, SE`.

**Strengths**:
* Electricity-bill worked example with `\hat{M}=142, \hat{S}=30, n=36` is concrete and complete.
* Coverage simulation with red/black lines for missed intervals is visually striking.
* Includes one-sided intervals and prediction intervals — both often skipped at this level.

**Weaknesses / gaps**:
* No `## Introduction`.
* Switches between `M` (estimator) and `\hat{M}` (estimate) in `M ± E` formulas without flagging the difference.
* The Normal-approximation CI's accuracy issue ("the sampling distribution might be far from normal") is mentioned once but never illustrated. A small Cauchy-like or heavily skewed example contrasted against a normal approximation would help.
* The "Sampling Distribution Quantiles" subsection uses 1000 obs per sample, which is huge for an intro example; might confuse students into thinking CIs require huge samples.
* "Test Yourself" with `se_boot` substitution is good but the rest of the chapter doesn't reinforce the bootstrap-SE substitution.
* Exercises are reasonable. The 99% vs 90% comparison is good. Bootstrap CI for median in R is good.

### 01_08 HypothesisTests (412 lines)

**Concepts**: hypothesis test, invert CI, impose null via bootstrap shift, p-value, caveats on p-values, t-value, quantile/shape statistics, one-sided tests.

**Datasets**: USArrests.

**Notation**: `H_0, H_A, p, \hat{F}^{boot}_0, \hat{t}, \mu, \mu_0, \hat{M}`.

**Strengths**:
* Two complementary methods (invert CI and impose null) presented clearly.
* p-value caveats are explicit: "the probability the null is true" misreading is explicitly debunked.
* The p-value simulation across 300 bootstraps shows that p-values are themselves random — this is good.
* t-statistic introduction sets up Part 2.
* The "recentering doesn't matter for one-sided tests" subtlety is shown via code, which is the right move.

**Weaknesses / gaps**:
* No `## Introduction`.
* "Caveats" is a subsection inside `## p-values`, but a similar-importance "Other Statistics" is its own section. Hierarchically odd.
* The bootstrap-shift formula `mean_b <- mean(dat_b) + (mu - sample_mean)` is correct but never explicitly named: the comment says "Bootstrap shift". A two-line callout could spell out *why* shifting works.
* The hypothesized `\mu_0 = 9` is contrived (USArrests Murder mean is ~7.79). A more economic-sounding hypothesis would be motivating.
* One-Sided Tests section is somewhat brief; only right-tail is shown numerically. Left-tail formula is stated but never run.
* Exercises are good: terminology, t-by-hand, bootstrap on USArrests Assault.

### 01_09 AdvancedProbability (521 lines)

**Concepts**: Binomial, Poisson, large-sample approximations (de Moivre–Laplace, Poisson Limit Theorem), Irwin–Hall, Beta, set theory (union/intersection/exclusivity/inclusion–exclusion/independence/conditional), Bayes' theorem, Law of Total Probability.

**Datasets**: synthetic (store / customer running example), six-sided die.

**Notation**: `\binom{n}{x}, \lambda, A \cup B, A \cap B, P(A|B), \lnot B`.

**Strengths**:
* Store/customer running example unifies Binomial and Poisson exposition.
* Poisson Limit Theorem derivation walks through the three limit steps clearly.
* Binomial-vs-Poisson-vs-Normal triple-overlay plot is excellent pedagogy.
* Bayes-theorem supplier example highlights the key insight (60% market share → 47% of defects).

**Weaknesses / gaps**:
* **Missing `***` after the title.**
* No `## Introduction`.
* **Broken sentence on line 17**: "If the coin is unfair; probability of heads equals $0.25$, then the corresponding outcomes $\{2,1,1,0\}$ have probability". Sentence is truncated, no answer given. Top priority to fix.
* Section heading `## Continuous Factorial Distributions` is a misnomer — Beta is not "factorial". Could be `## Continuous Compound Distributions` or just `## More Continuous Distributions`.
* "Test Yourself: Show that `E[X_i] = np`" — this proof is hard for an intro student; could be a guided derivation rather than open prompt.
* The "Test Yourself" Poisson `E[X_i] = V[X_i] = λ` proof is similarly hard; same suggestion.
* Set-theory die example is good but dense; the six-sided die both for the section and again for the Law of Total Probability could be visually separated.
* Law of Total Probability section is short and the bullet-point list at the top has a missing newline (in the file, the bullets run together).
* Exercises good — Poisson assumption critique, lambda=6 by hand, warpbreaks Poisson fit.

---

## Gaps vs a standard intro stats text

* **Sampling distributions for proportions**: implicit in Bernoulli-mean treatment but never explicitly framed as "the sampling distribution of $\hat{p}$ is approximately Normal with mean $p$ and SE $\sqrt{p(1-p)/n}$". ToDo.md flags this as desired.
* **One-sided intervals**: present in 01_07 but ToDo.md flags as needing updating. Section is shorter than two-sided treatment.
* **`X_i / x_i, \bar{X}/\bar{x}` notation choice**: ToDo.md suggests reconsidering. Currently the book uses `\hat{X}_i` for realization and `X_i` for random variable, plus `\hat{M}` for mean. This is internally consistent but unusual; many texts use lower-case `x_i` for realization and upper-case `X_i` for random variable. The memory file says to keep existing notation rather than rename, so flag only.
* **Inequalities (Chebyshev, Samuelson, 68/95/99.7)**: not mentioned in Part 1. ToDo.md flags as future work for "Misc Univariate Topics" — could go in 01_09 if we want.
* **Empirical mean ≠ population mean intuition**: covered via LLN; fine.
* **Hypergeometric / Negative Binomial / Gamma**: not in Part 1; appropriate for this level.

---

## Style-guide deviations summary

* **Chapter skeleton** (per `Code/callout_style_guide.md`): 01_06 violates `# Title` / `***`. 01_09 missing `***`. 7 of 9 chapters missing `## Introduction`.
* **`####` subsection format `**Name**. {-}`**: 01_06's first heading `## Statistical Theory` is at section level when it should be inside a chapter. All other `####` follow the bold-name-period-dash pattern. Good.
* **Callout class / title / icon / collapse**: spot-checked all callouts; ~50–60 total across Part 1; two use `collapse="false"` (01_03 weighted quantiles, 01_06 weighted variance). Style guide says default is `"true"`, exception is OK but should be deliberate.
* **No `###`**: confirmed none used.
* **Single-quote strings in R**: confirmed throughout.
* **`<-` assignment**: confirmed throughout.

---

## Summary scorecard

| Chapter | Has title+`***` | Has `## Introduction` | Numerical examples for math | Callout count (note+tip) | Major content gap |
|---|---|---|---|---|---|
| 00_01 First Steps | ✓ | ✗ | n/a (no math) | 2 | None — could deepen functions section |
| 01_02 Data | ✓ | ✗ | strong (histogram, ECDF, quantile worked) | 6 | None |
| 01_03 Descriptive | ✓ | ✓ | weak for skew/kurtosis; strong for mean/var/IQR | 9 | Skew/kurtosis hand-calcs; clusters section thin |
| 01_04 RandomVars | ✓ | ✓ | mixed (in/out probs not worked numerically) | 8 | Probability rules need a worked example |
| 01_05 Sampling | ✓ | ✗ | strong (Hesterberg, ages, SE) but **bug in SE example** | 11 | Two callouts mislabelled; SE numbers wrong |
| 01_06 PopStatistics | **✗** | ✗ | strong for discrete; weak for continuous | 7 | Missing chapter title; continuous E[X] |
| 01_07 Intervals | ✓ | ✗ | strong (electricity bill) | 5 | None major |
| 01_08 HypothesisTests | ✓ | ✗ | strong | 7 | None major |
| 01_09 AdvProbability | ✓ (no `***`) | ✗ | strong (Binomial, Poisson worked) | 11 | **Broken sentence**; section misnamed |

Total Part 1 callouts: ~66. Distribution looks fine; every chapter exceeds the 3–5 minimum.
