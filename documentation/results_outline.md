# Results Outline


## Static Analysis

### Simple summary
p(gamble) descriptives (group mean, range of individual means, s.d.)
reaction time descriptives (group mean/median, range of individual means/medians, s.d.)

### Parameter Estimation
Brief model summary w/ Rho, Mu
Describe the two fitting procedures (grid search; max LL)

#### Grid
How grid search worked (recap, brief)
Grid search results (mean & SEM rho & mu parameters; ranges of rho; ranges of mu)

#### Comparison to optimization
Optimization results (mean & SEM of rho & mu parameters; ranges of rho; ranges of mu)
Comparison of grid search to optimization (correlation; paired t-test; reference to supplementary figure)


## Digit Span
Brief task summary (i.e. forward, backward) & scoring approach summary.
Forward best span (mean, SEM, range)
Backward best span (mean, SEM, range)
Comparison of forward to backward (paired t-test, correlation, reference to supplementary figure)
Best Span overall (mean, SEM, range)
Categorical Span (high/low split)


## Dynamic Analysis
Analysis focus & plan: easy, difficult (define, describe setup)

### Simple Summary

#### Choices
mean p(gamble) by category (easy acc, easy rej, diff)
**FIGURE (histogram of p(gamble) by category)**
Comparison of easy acc & easy rej. in terms of distance from chance (definition of distance from chance; paired t-test; correlation, reference to supplementary figure) --> easy category
*-->implies that there's lots of individual variability in how people experienced difficult trials.*

#### Reaction Time

##### Simple Summary
mean reaction time by easy, difficult categories (mean of medians & SEM, paired t-test, correlation)
**FIGURE (scatter plot of median RT in easy vs. difficult)**
--> difficulty & ease follow expectations re: effort

##### Variance
Hypothesis: easy is easy, but difficult varies, implies more variability within and across participants in difficult trials than in easy.
WITHIN PERSON (mean of individual variances in RT in difficult trials vs. that in easy trials; paired t-test)
*--> Difficult trials had more variability within-person, whereas easy trials were more consistent. This implies that not all difficult trials were experienced in exactly the same way for a given person.*
ACROSS PERSON (variance of mean RTs in difficult trials vs. that of easy trials; var.test)
*--> Difficult trials have significantly more inter-individual variability, implying that difficult trials are experienced differently for different people, in alignment with our hypothesis.*

##### Regressions of RT
**Basic Categorical** (`m0rfx`): easy vs. difficult category predicts RTs (note that a similar pattern appears when only considering dynamic trials, see suppl.)

Calculation of continuous difficulty metric given optimized parameters. Neatly accounts for experienced difficulty across both static & dynamic trial types, allowing greater pooling of data & statistical power. 

**Basic Continuous** (`m1_allcont_rfx`): Replicates categorical take.

**Relationship of Categorical difficulty to Categorical Span** (`m1_capacityCatDiff_intxn_rfx`): Main effect of easy/difficult remains, no main effect of span group, but sig. interaction. UNPACK: implied mean(RT) by group. See supplementary for additional analysis
`sqrtRT ~ 1 + easyP1difficultN1 * capacity_HighP1_lowN1 + (1 | subjectnumber)`

**Relationship to Continuous difficulty to Categorical Span** (`m1_capacityContDiff_intxn_rfx`): Replicates categorical take (just note that sign has flipped b/c of variable coding!). Difficult trials are slower, and are even slower for high-capacity people.
`sqrtRT ~ 1 + all_diff_cont * capacity_HighP1_lowN1 + (1 | subjectnumber)`

**Relationship with Continuous Span** (`m1_diffCat_capacityCont_intxn_rfx` and `m1_diffCont_capacityCont_intxn_rfx`): No interaction of difficulty (continuous or categorical) with continuous span, suggesting that there may be a threshold level of digit span instead of a more continuous relationship. That would be consistent with this task being of a consistent and low-to-moderate complexity.

**TAKEAWAY:** The experience on trials that were designed to be easy vs. difficult appears to match reaction times. While digit span (aka capacity) did appear to matter, the sign of the relationship was inverse to predictions. 

##### Sequential Effects
Additional predictions of previous ease & difficult influencing choices on subsequent trial types. Modified regressions above to include previous difficult in addition to current difficult (and span where applicable).

**Basic Categorical w/ Prev. Categorical**

**Basic Continuous w/ Prev. Continuous**

**Relationship of Categorical difficulty & Prev. Categorical Difficulty to Categorical Span**

**Relationship of Continuous difficulty & Prev. Continuous Difficulty to Categorical Span**

**TAKEAWAY:**

## SUPPLEMENT
- Suppl. Fig: Grid Search vs. Optimization (4 part plot: for each of rho & mu: scatterplot [grid vs. opt]; histogram of difference in parameters)
- Suppl. Fig: Scatter plot of forward vs. backward span.
- Suppl. Fig: Scatterplot of distance from chance easy acc vs. easy rej

### Supplemental models
**Basic Cat but only Dynamic** (`m0_cat_dynonly_rfx`)

**Basic Cont but only Dynamic** (`m1_cont_dynonly_rfx`)

**Categorical Span x easy and Categorical span x difficult** (`m1_capacityCat_intxn_rfx`) (note: trending effect of high capacity individuals being slower on difficult trials, no effect on easy trials)
`sqrtRT ~ 1 + easy * capacity_HighP1_lowN1 + difficult * capacity_HighP1_lowN1 + (1 | subjectnumber)`

**Relationship of Categorical difficulty & Prev. Categorical Difficulty to Continuous Span**

**Relationship of Continuous difficulty & Prev. Continuous Difficulty to Continuous Span**
