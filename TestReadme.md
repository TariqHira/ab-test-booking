✈️ A/B Testing Flight Booking Conversion Rates
🌟 A practical data science project simulating an A/B test to evaluate the effect of a new pricing strategy on flight booking conversions — set in the context of an imaginary travel platform, MyTravel.com.

📌 Project Overview
The Flight Booking Team at MyTravel.com has rolled out a new pricing strategy. To assess whether this strategy is actually increasing flight bookings — or if the observed change is simply due to chance — they've tasked Miss Reem, a Data Scientist, with designing and conducting a hypothesis test.

Miss Reem's job isn't just to crunch numbers; it's to ensure the experiment is statistically and practically significant, the data is analyzed rigorously, and the results are interpreted in a way that guides strategic decisions.

This project takes you through a realistic workflow:

Simulate user-level booking data

Design and implement an A/B test

Apply hypothesis testing

Visualize and interpret results

All with the goal of helping data professionals build intuition and confidence in experimentation.

👥 Target Audience
This project is designed for:

Aspiring or working Data Scientists, Analysts, and Product Managers

Candidates preparing for A/B testing or product analytics interviews

Learners looking to understand and apply hypothesis testing in a practical setting

🧪 Why Hypothesis Testing?
The key question in business often is:

“Is the observed improvement real or just random noise?” In business, we frequently want to validate if a new strategy truly creates an improvement. But natural variation makes this tricky — especially for proportions (e.g., booking conversion rates).

That’s where hypothesis testing comes in.

🔍 What is Hypothesis Testing?
Miss Reem knows that it's impossible and impractical to run the experiment on the entire population. Instead, she can run an experiment on selected samples from the population. She's also well aware of the statistical method "hypothesis testing," which is used to make decisions or inferences about population parameters based on sample data. The process involves:

Formulating two hypotheses:

Null Hypothesis (H_0): Assumes no effect or no difference (e.g., "There is no difference in conversion rates between the control and treatment pages").

Alternative Hypothesis (H_1): Assumes there is an effect or a difference (e.g., "The new pricing page increases conversions").

Designing the Experiment: Estimating the Sample Size based on Minimum Detectable Effect, Power, and Significance.

Collecting data from experiments or observations.

Analyzing the data to determine whether the evidence is strong enough to reject the null hypothesis in favor of the alternative.

🧪 What is A/B Experimentation?
Miss Reem decides to implement an A/B test — a practical form of hypothesis testing. It compares two versions (A and B) of a feature by randomly splitting users and measuring which performs better on a defined metric (like conversion rate).

📊 Two-Proportion Hypothesis Testing (A/B Experiment)
Two-Proportion Hypothesis Testing is used to determine if there is a statistically significant difference between the proportions of a certain characteristic (e.g., conversion rate) in two independent groups.

When to Use It:

You have two independent samples (e.g., control vs. treatment).

Each sample yields a proportion (e.g., % of users who book flights).

You want to know if the difference in these proportions is due to chance.

|

| Group | Description |
| A | Control Group |
| B | Treatment Group |

Null Hypothesis (H_0): Conversion Rate of Group B 
le Conversion Rate of Group A

Alternative Hypothesis (H_1): Conversion Rate of Group B  Conversion Rate of Group A (one-tailed)

🎯 One-Tailed vs. Two-Tailed Tests
The choice of a one-tailed or two-tailed alternative hypothesis is critical.

One-Tailed Test (H_1:p_Bp_A or H_1:p_B\<p_A): This is used when you are only interested in detecting an effect in a specific direction. For example, if the new pricing strategy is only considered successful if it increases conversions, a one-tailed test is appropriate. It offers more statistical power to detect an effect in the specified direction. This means the rejection region for the null hypothesis is entirely in one tail of the sampling distribution.

Two-Tailed Test (H_1:p_B
neqp_A): This is more common in exploratory A/B testing as it can detect a significant difference in either direction (increase or decrease). If you're unsure whether the new strategy might increase or decrease conversions, or if a decrease would also be an important finding, a two-tailed test is more suitable. The rejection region is split between both tails of the sampling distribution.

In this project, a one-tailed test is chosen, implying that the team is primarily interested in detecting a positive uplift in conversion rates.

📝 Assumptions for Two-Proportion Z-Test
For the results of a two-proportion Z-test to be reliable, certain assumptions should be met:

Independence of Observations: The outcomes for one user should not influence the outcomes for another user. This is typically ensured by random assignment to groups.

Independent Samples: The two groups (control and treatment) must be independent of each other.

Large Enough Sample Size: For the sampling distribution of the proportions to be approximately normal (allowing the use of Z-scores), the number of "successes" and "failures" in each group should be sufficiently large (a common rule of thumb is at least 10 in each category: n_Ap_A
ge10, n_A(1−p_A)
ge10, n_Bp_B
ge10, n_B(1−p_B)
ge10).

📏 Understanding Effect Size: Cohen's d and Cohen's h
Beyond just statistical significance, it's crucial to understand the magnitude or strength of an observed effect. This is where effect size measures come in.

Cohen's d (for continuous data):

When to use: Cohen's d is used when comparing the means of two groups on a continuous variable (e.g., average revenue per user, time spent on page). It expresses the difference between two means in terms of standard deviation units.

Formula: d=
fracbarx 
1
​
 −barx 
2
​
 s 
p
​
  where 
barx 
1
​
  and 
barx 
2
​
  are the means of the two groups, and s 
p
​
  is the pooled standard deviation.

Interpretation:

d=0.2: Small effect

d=0.5: Medium effect

d=0.8: Large effect

Cohen's h (for proportions):

When to use: Cohen's h is specifically designed for comparing two proportions, which is highly relevant for A/B testing conversion rates. It's a measure of effect size that accounts for the non-linear nature of proportions by using an arcsine transformation.

Formula: h=2
cdot(
arcsin(
sqrtp 
1
​
 )−
arcsin(
sqrtp 
2
​
 ))

Where p 
1
​
  and p 
2
​
  are the two proportions being compared (e.g., control conversion rate and treatment conversion rate).

Interpretation: Similar to Cohen's d, general guidelines are:

h=0.2: Small effect

h=0.5: Medium effect

h=0.8: Large effect

Why arcsin transformation? This transformation helps normalize the variance of proportions, making the effect size more consistent across different baseline rates.

🧪 Designing the Experiment
As a Data Scientist, Miss Reem makes careful decisions regarding:

✅ A/B Test Design Checklist
Define the Business Impact (Minimum Detectable Effect - MDE):

What uplift (e.g., +5% conversion) is meaningful to detect? The MDE is not just a statistical parameter; it's a business decision. It represents the smallest change that would be considered financially or strategically worthwhile to implement. For instance, a 0.5% conversion uplift might be statistically significant but not justify the development and maintenance costs.

Calculating MDE: If your baseline conversion rate (p 
1
​
 ) is known, and you define the MDE as a percentage uplift of that baseline, you can calculate p 
2
​
 .

Example: If baseline (p 
1
​
 ) is 10% (0.10) and you want to detect a 5% relative uplift, then the desired conversion rate in the treatment group (p 
2
​
 ) would be p 
1
​
 
cdot(1+
textrelativeMDE)=0.10
cdot(1+0.05)=0.105 (or 10.5%).

If the MDE is given as an absolute difference (e.g., an absolute increase of 5 percentage points), then p 
2
​
 =p 
1
​
 +
textabsoluteMDE. For example, if p 
1
​
 =0.10 and absolute MDE is 0.05, then p 
2
​
 =0.10+0.05=0.15 (or 15%).

Estimate Baseline (p_1):

Use historical data (last campaign, last month, etc.) to get an accurate estimate of the current conversion rate.

Choose Acceptable 
alpha and Power:

Standard values: 
alpha=0.05 (Significance Level), Power = 0.80 (or 80).

Use Power Analysis Tool to get Minimum Sample Size:

statsmodels.stats.power in Python

Online calculators like Evan Miller's A/B Test Calculator

The goal is either to Reject the Null Hypothesis if it's not true (related to the Power of a Test) or Do Not Reject it if it is, in fact, true, based on the test results. If the test is poorly designed, the results can be biased and lead to the following errors.

🚨 Type I and Type II Errors
| Error Type | Description | Controlled by | Example |
| Type I | False positive — reject H_0 when it’s true | Significance level 
alpha | You say B  A, but it’s not |
| Type II | False negative — fail to reject H_0 when it’s false | Power = 1−
beta | You say B = A, but B is better |

🛡️ How to Avoid:
Type I: Choose small 
alpha (e.g., 0.01 or 0.05)

Type II: Choose higher power (e.g., 0.90), increase sample size

Pre-registration: Fix 
alpha, power, and sample size before starting the experiment.

🧪 Summary of Key A/B Testing Terms
| Term | Meaning |
| Power | Probability of detecting a true effect (1−
beta) |
| Type I Error (
alpha) | Rejecting a true null hypothesis |
| Type II Error (
beta) | Failing to reject a false null hypothesis |
| Effect Size | The actual difference between p_1 and p_2 (often the MDE), or Cohen's h for proportions |
| Sample Size | Larger sample 
rightarrow lower 
beta
rightarrow higher power |

🧮 Sample Size Formula for Two Proportions
The formula for calculating the minimum sample size (n) required per group for comparing two proportions is derived from power analysis. It ensures you have enough data to detect a statistically significant difference (the MDE) with your chosen alpha and power levels.

The general formula for sample size per group (assuming equal group sizes, n 
A
​
 =n 
B
​
 =n) is:

n=
left[
fracZ 
1−alpha/t
​
 cdotsqrt2p(1−p)+Z 
1−beta
​
 cdotsqrtp 
1
​
 (1−p 
1
​
 )+p 
2
​
 (1−p 
2
​
 )p 
1
​
 −p 
2
​
 
right] 
2
 

Where:

p=
fracp_1+p_22 (pooled proportion under the null hypothesis, assuming p 
1
​
 =p 
2
​
 )

p_1 = baseline conversion rate (control group)

p_2 = expected conversion rate in the treatment group (p_1+
textMDE)

Z_1−alpha/t = The critical Z-value corresponding to the chosen significance level (
alpha). The 't' in the subscript indicates whether it's a one-tailed or two-tailed test.

For a one-tailed test: Z_1−alpha (e.g., for 
alpha=0.05, Z_1−0.05
approx1.645)

For a two-tailed test: Z_1−alpha/2 (e.g., for 
alpha=0.05, Z_1−0.025
approx1.96)

Z_1−beta = The critical Z-value corresponding to the desired power (1−
beta). For a power of 0.80, Z_1−0.80
approx0.84.

Intuition Behind the Formulas:

Numerator: The numerator involves the Z-scores for alpha and beta, and the standard errors of the proportions. It represents the "signal" needed to detect the effect, scaled by variability.

Z 
1−alpha/t
​
  accounts for the risk of a Type I error. A smaller 
alpha (e.g., 0.01 instead of 0.05) means a larger Z-value, requiring a larger sample size to achieve that stricter confidence.

Z 
1−beta
​
  accounts for the desired power. A higher power (e.g., 0.90 instead of 0.80) means a larger Z-value, requiring a larger sample size to increase the chance of detecting a true effect.

The square root terms represent the variability (standard error) of the proportions. Higher variability requires larger samples.

Denominator: The denominator is the square of the difference between the two proportions (p 
1
​
 −p 
2
​
 ), which is essentially your Minimum Detectable Effect (MDE).

A smaller MDE (i.e., you want to detect a very subtle difference) means a smaller denominator, which in turn requires a much larger sample size. This makes intuitive sense: it's harder to reliably detect a tiny difference than a large one.

You can calculate this manually or using Python libraries like statsmodels.stats.power.

Calculating Sample Size from Cohen's h (Effect Size for Proportions):

While the formula above directly uses p 
1
​
  and p 
2
​
 , Cohen's h is the effect size for proportions. You would typically calculate Cohen's h from your p 
1
​
  and p 
2
​
  (where p 
2
​
 =p 
1
​
 +MDE) and then use power analysis tools (like statsmodels.stats.power.GofChisquarePower().solve_power in Python) that accept effect size (h), alpha, and power as inputs to determine the sample size.

If you don't know the baseline (p 
1
​
 ), calculating a meaningful sample size for an A/B test on proportions becomes challenging because the variability of proportions depends on their values. In such a scenario, you would typically:

Conduct a pilot study: Run a small preliminary experiment to get an estimate of the baseline conversion rate.

Use industry benchmarks: If available, use conversion rates from similar products or industries as a proxy for your baseline.

Define a hypothetical baseline: For purely theoretical exercises, you might assume a baseline.

Once you have an estimated p 
1
​
  and your desired MDE (which gives you p 
2
​
 ), you can calculate Cohen's h and then use it in sample size calculations.

📈 Beyond the P-value: Confidence Intervals
While the p-value tells us if an observed difference is statistically significant, it doesn't tell us the magnitude of that difference. This is where confidence intervals become invaluable.

A confidence interval provides a range of plausible values for the true difference in conversion rates between the control and treatment groups. For example, a 95% confidence interval for the difference might be [0.02,0.08], meaning we are 95% confident that the true uplift is between 2% and 8%.

Why use it? A confidence interval gives a more complete picture than just a p-value. It helps in understanding the practical significance of the results and can guide business decisions more effectively. If the confidence interval includes zero, it implies no statistically significant difference.

🛠️ Practical Considerations for A/B Testing
Designing and running an A/B test involves more than just statistical formulas. Miss Reem also needs to consider practical aspects:

Experiment Duration: How long should the test run? Running a test for too short a period can lead to misleading results due to novelty effects (users reacting differently to a new feature simply because it's new) or day-of-week biases. Running it too long can delay decision-making. A typical duration is 1-2 full business cycles (e.g., 1-2 weeks).

Contamination: What if users clear their cookies, use multiple devices, or are exposed to both the control and treatment versions? These factors can contaminate the experiment and bias results. Robust tracking and user identification strategies are crucial.

External Factors: Be aware of external events (e.g., holidays, marketing campaigns, competitor actions) that could influence conversion rates during the experiment period.

Sequential Testing: For long-running experiments or when quick decisions are needed, more advanced techniques like sequential testing can be considered. These methods allow for continuous monitoring of results and can enable stopping the experiment early if a clear winner (or loser) emerges, potentially saving time and resources. However, they require specific statistical adjustments to maintain the desired 
alpha level.