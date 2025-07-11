# ✈️ A/B Testing Flight Booking Conversion Rates

> 🌟 A practical data science project simulating an A/B test to evaluate the effect of a new pricing strategy on flight booking conversions — set in the context of an imaginary travel platform, **MyTravel.com**.

---

## 📌 Project Overview

The **Flight Booking Team at MyTravel.com** has rolled out a new pricing strategy. To assess whether this strategy is actually increasing flight bookings — or if the observed change is simply due to chance — they've tasked **Miss Reem**, a **Data Scientist**, with designing and conducting a hypothesis test.

Miss Reem's job is not just to crunch numbers, but to ensure the experiment is statistically as well as practically significant, the data is analyzed rigorously, and the results are interpreted in a way that guides strategic decisions.

This project takes you through a realistic workflow:

- Simulate user-level booking data
- Design and implement an A/B test
- Apply hypothesis testing
- Visualize and interpret results

All with the goal of helping data professionals build intuition and confidence in experimentation.

---

## 👥 Target Audience

This project is designed for:

- Aspiring or working **Data Scientists**, **Analysts**, and **Product Managers**
- Candidates preparing for **A/B testing or product analytics interviews**
- Learners looking to **understand and apply hypothesis testing in a practical setting**

---

## 🧪 Why Hypothesis Testing?

In any A/B test, the key question is:

> “Is the observed improvement real or just random noise?”

That’s where **hypothesis testing** comes in.

### 🔍 What is Hypothesis Testing?

Miss Reem knows that hypothesis testing is a statistical method used to make decisions or inferences about population parameters based on sample data. The process involves:

- **Formulating two hypotheses:**

  - **Null Hypothesis (H₀):** Assumes no effect or no difference (e.g., "There is no difference in conversion rates between the control and treatment pages").
  - **Alternative Hypothesis (H₁):** Assumes there is an effect or a difference (e.g., "The new pricing page increases conversions").

- **Collecting data** from experiments or observations.

- **Analyzing the data** to determine whether the evidence is strong enough to reject the null hypothesis in favor of the alternative.

## 📊 Two-Proportion Hypothesis Testing (A/B Experiment)

Two Proportion Hypothesis Testing is used to determine if there is a statistically significant difference between the proportions of a certain characteristic (conversion rate) in two independent groups.

**When to Use It:**

- You have two independent samples (e.g., control vs. treatment).
- Each sample yields a proportion (e.g., % of users who book flights).
- You want to know if the difference in these proportions is due to chance.

| Group | Description     |
| ----- | --------------- |
| A     | Control Group   |
| B     | Treatment Group |
| Null Hypothesis (H₀)     | Conversion Rate of Group B ≤ Conversion Rate of Group A   |
| Alternative Hypothesis (H₁)     | Conversion Rate of Group B > Conversion Rate of Group A (one-tailed) |



After defining the hypotheses, Miss Reem proceeds to design the experiment. For this she precisely calculate the **minimum sample size** needed to detect an effect size (uplift) with sufficient statistical **power** and **significance level**.

---

## 🧪 Designing the Experiment

As a Data Scientist, Miss Reem makes careful decisions regarding:

### ✅ A/B Test Design Checklist

- **Define the Business Impact:**

  - What uplift (e.g., +5% conversion) is meaningful to detect?

- **Estimate Baseline (p₁):**

  - Use historical data (last campaign, last month, etc.)

- **Choose Acceptable α and Power:**

  - Standard: α = 0.05, Power = 0.80

- **Use Power Analysis Tool to get Minimum Sample Size:**

  - `statsmodels.stats.power` in Python
  - Online calculators like [Evan Miller's A/B Test Calculator](https://www.evanmiller.org/ab-testing/sample-size.html)

### 🚨 Type I and Type II Errors

| Error Type | Description                                        | Controlled by        | Example                        |
| ---------- | -------------------------------------------------- | -------------------- | ------------------------------ |
| Type I     | False positive — reject H₀ when it’s true          | Significance level α | You say B > A, but it’s not    |
| Type II    | False negative — fail to reject H₀ when it’s false | Power = 1 − β        | You say B = A, but B is better |

### 🛡️ How to Avoid:

- Type I: Choose small α (e.g., 0.01 or 0.05)
- Type II: Choose higher power (e.g., 0.90), increase sample size
- Pre-registration: Fix α, power, and sample size before starting

### 🧪 Summary Table

| Term              | Meaning                                        |
| ----------------- | ---------------------------------------------- |
| Power             | Probability of detecting a true effect (1 - β) |
| Type I Error (α)  | Rejecting a true null hypothesis               |
| Type II Error (β) | Failing to reject a false null hypothesis      |
| Effect Size       | Difference between p₁ and p₂                   |
| Sample Size       | Larger sample → lower β → higher power         |

### 🧮 Sample Size Formula (for One-Tailed Test)

```math
n = \left[ \frac{Z_{1−\alpha} \cdot \sqrt{2p(1−p)} + Z_{1−\beta} \cdot \sqrt{p_1(1−p_1) + p_2(1−p_2)} }{p_1 − p_2} \right]^2
```

Where:

- \(p = \frac{p_1 + p_2}{2}\)
- \(Z_{1−\alpha}, Z_{1−\beta}\) = critical z-values for significance level and power

You can calculate this manually or using Python libraries.

---

