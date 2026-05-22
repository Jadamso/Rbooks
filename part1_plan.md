# Part 1 Improvement Plan (Phase 2)

Prioritized improvements for Part 1 (Stats I), derived from `part1_analysis.md`.
Each chapter lists items as **High**, **Medium**, or **Low** impact.

---

## Interpretation notes (ambiguous task items)

These decisions were made where the task focus, `ToDo.md`, the style guides, and the
current book state conflicted. They are stated here so reviewers can override.

1. **Functions / logic / counting placement.** The focus says to add "what a function
   is", logic, and counting to `01_02_Data`. But `00_01_FirstSteps` already has full
   sections on functions and logic, `01_05_Sampling` already introduces
   `choose`/`factorial`/permutations, and `01_02` is at the 13-subsection cap (the focus
   itself says not to add subsections there). **Decision:** the three combinatorics
   problems (license plates, bank accounts, HR committee) and explicit counting rules go
   into `01_05_Sampling`, extending its existing permutations / binomial-coefficient
   material. Functions and logic are left in `00_01` (no duplication). `01_02` gets no
   new subsections. This keeps counting adjacent to the binomial coefficient (01_05) and
   the Binomial distribution (01_09), which is the natural pedagogical order.

2. **`## Introduction` headers.** The callout style guide mandates `## Introduction`, but
   only 6 of ~27 content chapters in the whole book actually have one. Adding the header
   to the 6 Part 1 chapters that lack it would make Part 1 *inconsistent with the rest of
   the book* and counts as restructuring, which the task forbids. **Decision:** do not
   add `## Introduction` headers. Where a chapter opens abruptly, improve the existing
   opening prose instead.

3. **`01_06` chapter title.** The file currently has no `#` title and no `***` rule — it
   starts at `## Statistical Theory`. This is a genuine defect (the rendered page has no
   title). **Decision:** add `# Population Statistics` + `***`. Keep `## Statistical
   Theory` as the first section (its content — the estimate/estimator/parameter
   distinction — is correctly named).

4. **Code-style standardization.** The focus says "standardize code style," but the task
   also says "Do NOT rewrite code blocks unless they are broken or misleading."
   **Decision:** apply the R style guide only to *new* code added in this pass, and to
   genuinely broken code. No sweep of existing working code (e.g., `1:n` vs `seq` is left
   alone).

5. **"Mark definitions in markdown alongside italics."** The style guide defines no
   "definition callout" type (`ToDo.md` lists it only as an open question).
   **Decision:** interpret this as "ensure every first-use term is italicized with
   `*term*`." No new callout type is invented.

6. **Stale focus items.** One-sided intervals (`01_07`) and the Poisson section (`01_09`)
   already exist in substantial form — the focus list appears to predate the current
   chapter state. These will be reviewed and polished, not rebuilt.

---

## Cross-chapter items

- **CR1 (High).** `01_06` missing `#` title + `***`; `01_09` missing `***`. Fix both.
- **CR2 (Medium).** Add high-value cross-references:
  `01_03` → `01_02` (quantiles/median); `01_06` → `01_05` (bootstrap loop);
  `01_07` → `01_05` (bootstrap distribution); `01_08` → `01_07` (inverting a CI).
  Use the existing `https://jadamso.github.io/Rbooks/CHAPTER.html#section` format.
- **CR3 (Low).** `01_02` introduces `\hat{X}_i` cold. Add one clarifying sentence that
  the hat marks a value computed from observed data (formalized in `01_06`). Do not
  rename the notation.

---

## 00_01 First Steps

**High**
- Typo in a key definition: line 9 reads `*Reproducibile*` — correct to `*Reproducible*`.
- Only 2 callouts (both are deliberate format demos). Task requires 3–5 *content*
  callouts. Add a `callout-note` "Must Know" in the Functions section with a genuinely
  useful one-line custom statistic (e.g. a `range`-style helper), and a `callout-tip`
  "Test Yourself" in the Loops/Logic area asking the student to predict loop output.

**Medium**
- `## Mathematical Functions` → the `add_two` example never shows *why* functions are
  useful. The new Must Know callout (above) addresses this by computing a real statistic.
- Line 7: "You also want your work to be replicable" — sentence has no period. Fix.

**Low**
- `## Mathematical Objects` opens with one short line; add a sentence of framing so the
  section does not start mid-thought.
- `# Common Functions`: `# ?sum` is commented out; the prose says "see exactly what a
  function does with `?`". Leave the code as-is (not broken) but the prose is fine.

## 01_02 Data & Visualization

**High**
- Empirical mass function: the formula `\hat{p}_x = \sum 1(\hat{X}_i = x)/n` (line ~194)
  has no by-hand numerical example — only USArrests code. Add a small worked example
  (e.g. dataset `{1,2,1,3,1}` → `p_1 = 3/5, p_2 = 1/5, p_3 = 1/5`).

**Medium**
- Uniform-kernel density formula `k_U` (line ~310) has a visual but no by-hand number.
  Add a one-line numerical example (a point inside vs outside `[x-h, x+h]`).
- CR3: clarify `\hat{X}_i` on first use in the Proportions section.
- "Outer products yield arrays" code chunk (line ~147) is dangling — add a sentence of
  motivation so it is not an orphan.

**Low**
- Boxplot subsection: state explicitly "the box spans the IQR" alongside the existing
  prose so the figure is self-explaining.
- Mode is mentioned in passing in the quantiles callout before `01_03` defines it — add
  a short forward-reference rather than redefining.
- Do **not** add subsections (at the 13-subsection cap).

## 01_03 Descriptive Statistics

**High**
- Skewness formula (line ~326) has **no worked numerical example** — only code on
  `USArrests`. Add a `callout-note` worked example on a tiny dataset showing each step:
  mean, cubed deviations, their average, divide by `sd^3`. Compute consistently with the
  chapter's own `skewness()` function (which uses `sd()`).
- Kurtosis formula (line ~352) has the same gap. Add a parallel worked example (quartic
  deviations / `sd^4`).
- `#### Clusters/Gaps` is the weakest section in the chapter: two `echo=F` simulations
  and one sentence ("a picture is worth a thousand words"). Add real exposition —
  describe modes, bunching, what a multimodal histogram tells you — and make at least one
  simulation visible so the reader sees what is described.

**Medium**
- Jensen's inequality: the picture-intuition ("curve inwards like the inside of a cave")
  is good but thin. Add the formal one-line statement for concave `g`
  (`g(\hat{M}_X) \geq \hat{M}_Y`) next to it; the convex case is already stated.
- Mode subsection: narrate the existing frequency-table code so the worked example reads
  as prose, not just a code dump.
- CR2: when the median is introduced, back-link to the `01_02` quantiles section.

**Low**
- Weighted Quantiles callout uses `collapse="false"`; switch to `"true"` for
  consistency (style guide default).
- Note (do not change): `skewness()` mixes divide-by-`n` (`mean`) and divide-by-`n-1`
  (`sd`). Left as-is per "don't rewrite working code"; worked examples will match the
  code's behavior.

## 01_04 Random Variables

**High**
- **Focus item:** show explicitly how `F(x)` is built from `f(x)` and the reverse.
  Currently only `f → F` is stated in prose ("F(x) equals the area under the PDF").
  Expand the `## Continuous Random Variables` opening prose to also state `F → f` (the
  density is the slope of the CDF), and add a `callout-note` worked example on the
  Uniform: `f(x)=1` constant, `F(x)=x` linear — F accumulates area, f is the slope of F.
  Add one sentence in the discrete area noting `F` is the cumulative sum of the PMF.
- **Focus item:** complete the unfinished math-scores `callout-tip` (line ~500). It is
  currently a pure-prose question with `\mu=50, \sigma=1` — parameters that make every
  tail probability effectively 0, so the comparison teaches nothing, and it has no code.
  Repair the parameters so the answers are meaningful, interpretable probabilities, keep
  the "vary `\mu` and `\sigma`" intent, and add starter/solution code (`pnorm`).

**Medium**
- Exponential parameter is called the parameter "that governs its shape" (line ~365).
  It is the **rate** parameter (mean `= 1/\lambda`). Correct the wording to "rate" — the
  notation guide and `01_06` both use "rate". This is a terminology fix, not a rename.
- `#### Probability Rules` (line ~46) has dense in/out formulas and no example. Add a
  one-line numerical illustration or an explicit pointer to the four-sided-die Must Know
  that demonstrates them.

**Low**
- Normal PDF: after the formula, add a one-line plain-language description ("a bell
  shape centered at `\mu` with spread `\sigma`") before the code.
- Bernoulli: add a forward-reference noting `E[X_i]=p` is derived in Population
  Statistics.

## 01_05 Sampling & Resampling

**High**
- **Bug:** the bootstrap-SE worked example (line ~634) says "five bootstrap estimates
  `{8,5,4,7,8}`" but the calculation below uses `{3,5,6,7,9}` (which is what yields the
  stated mean 6 and SE 2). Fix the prose to `{3,5,6,7,9}`.
- The Jackknife and Bootstrap "Must Know" callouts (lines ~536, ~564) only pose a task
  ("compute the jackknife estimate of the median … by hand and with the computer") with
  no answer — so they read as exercises mislabeled as worked examples. Add the worked
  solution inside each (jackknife on `{1,6,7,22}`; bootstrap median with `B=8`) so they
  become genuine Must Know worked examples.
- **Focus item (relocated here — see Interpretation note 1):** add explicit counting
  rules and the three combinatorics problems. In the `## Sampling` section, after the
  existing permutations / binomial-coefficient callout, add prose on the multiplication
  rule and on permutations (order matters) vs combinations (order does not), then a
  `callout-note` working all three: (a) license plates `26·25·24·10·9·8`,
  (b) bank accounts `choose(20,3)`, (c) HR committee `25·24 · choose(23,5)`. No new
  `####` subsection — prose + callout inside `## Sampling`.

**Medium**
- CR2: no back-link to `01_03` when `median`/`sd` reappear as resampled statistics — add
  one.

**Low**
- `## Drawing Samples` (inverse sampling / Dagum) is advanced and disconnected, but
  removing/moving it is restructuring — leave it; optionally add one framing sentence.
- Cauchy "fat tails" chunk is `eval=F`; left as-is (not broken, deliberate).

## 01_06 Population Statistics

**High**
- **CR1:** add `# Population Statistics` + `***` (file currently starts at
  `## Statistical Theory`).

**Medium**
- The four-sided-die Must Know (line ~91) works the mean but leaves the variance as
  "What is the variance?" with no answer. Complete the variance computation
  (`V = 10/8 = 1.25`) and add the verifying simulation so it is a full worked example.
- `\mathbb{V}[M] = \sigma^2/n` and `SE(M) = \sigma/\sqrt{n}` (lines ~363–370) are derived
  but never shown on numbers. Add a one-line numerical example (e.g. `\sigma=10, n=4`
  → `SE = 5`).
- Weighted-variance `callout-tip` (line ~301) is `eval=F` and only says "Provide a
  concrete example." Complete it with a small worked weighted variance.
- CR2: back-link to `01_05` where the bootstrap loop is reused.

**Low**
- Two callouts use `collapse="false"`; switch to `"true"`.
- Add a one-sentence closing transition into `01_07` (intervals).

## 01_07 Confidence Intervals

**High**
- **Focus item:** add "fail to reject" / multiple-competing-hypotheses content. A CI
  contains many values, and *every* value inside it is a hypothesis that cannot be ruled
  out. Add a `callout-note` making this explicit: given a CI such as `[6.6, 9.0]`, you
  cannot rule out `\mu=7`, nor `\mu=8`, nor `\mu=8.9` — "fail to reject" is a statement
  about a whole range, not a single value. Forward-link to `01_08`.

**Medium**
- The first Must Know (line ~44) — "Compute a 90% CI and a 99% CI. Interpret each…" — is
  a bare prompt with no code. Add the worked CIs (the bootstrap object already exists
  just above) so it is a real worked example.
- Normal-approximation accuracy: line ~142 says the approximation can be poor "but that
  does not always need to be the case" without ever showing it. Add a brief illustration
  or at minimum a concrete sentence on *when* it fails (skewed / small `n`).
- CR2: back-link to `01_05` where the bootstrap distribution is first built.

**Low**
- One clarifying sentence distinguishing `M` (estimator) from `\hat{M}` (estimate) in the
  `M \pm E` formula — they are already used correctly, just not flagged.

## 01_08 Hypothesis Testing

**Medium**
- The bootstrap-shift `mean(dat_b) + (mu - sample_mean)` is used but only briefly
  explained inline. Add a short `callout-note` spelling out *why* shifting imposes the
  null (it moves the resampling distribution to be centered at `\mu_0` without changing
  its spread/shape).
- `## One-Sided Tests`: only the right-tail `p`-value is computed; the left-tail formula
  is stated but never run. Add the left-tail computation so both are demonstrated.
- CR2: back-link to `01_07` where "invert a CI" is introduced.

**Low**
- The "Caveats" subsection sits inside `## p-values` while the comparably-weighted
  "Other Statistics" is its own `##` — noted only; section hierarchy left unchanged.

## 01_09 Advanced Probability

**High**
- **CR1:** add `***` after `# Advanced Probability` (line 2 is currently blank).
- **Broken sentence, line 17:** "If the coin is unfair; probability of heads equals
  `0.25`, then the corresponding outcomes `{2,1,1,0}` have probability" — the sentence
  stops mid-clause with no answer. Complete it: for `p=0.25`, the outcomes
  `HH, HT, TH, TT` have probabilities `0.0625, 0.1875, 0.1875, 0.5625`, giving
  `Prob(X=0)=0.5625, Prob(X=1)=0.375, Prob(X=2)=0.0625`.

**Medium**
- Law of Total Probability section: missing blank line before the `- The sets are …`
  bullet (line ~497), so the list may not render. Fix the markdown.
- Poisson section (focus item) reviewed — already complete (PMF, CDF, by-hand
  probabilities, plots, mean/variance, lunch-rush example, shape variation). Polish
  wording only; no rebuild needed.

**Low**
- `## Continuous Factorial Distributions` is an odd name for Beta/Irwin–Hall, but
  renaming a section is restructuring — left unchanged, noted only.
- The "Show `E[X]=np`" / "Show `E[X]=V[X]=\lambda`" Test Yourself prompts are hard for
  an intro student; the Binomial one is already partly guided. Leave; optionally add one
  scaffolding sentence.

---

## Implementation order

File order, one commit per chapter, high-impact items first within each:
`00_01 → 01_02 → 01_03 → 01_04 → 01_05 → 01_06 → 01_07 → 01_08 → 01_09`.
Critical structural bugs (CR1, the `01_09` sentence, the `01_05` number bug) are fixed
as part of their chapter's commit.
