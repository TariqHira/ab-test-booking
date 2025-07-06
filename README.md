# ✈️ A/B Testing Flight Booking Conversion Rates

> **A professional data science project simulating an A/B test to evaluate the uplift in booking conversion rates for a new pricing strategy — inspired by the Flights Data Science team at Booking.com.**

---

## 📌 Project Overview

This project simulates and analyzes an A/B test scenario in the context of flight bookings, where a new pricing strategy is introduced to improve booking conversion rates.

Our goal is to answer:

> *"Is the observed uplift in booking rates due to the new pricing strategy statistically significant, or just due to random chance?"*

---

## 🧪 Why Hypothesis Testing?

In business, we often want to validate if a new strategy truly creates an improvement. But natural variation makes this tricky — especially for proportions (e.g., booking conversion rates).

So we use **hypothesis testing** to quantify our confidence:

- **Null Hypothesis (H₀):** No change (p1 = p2)
- **Alternative Hypothesis (H₁):** There is a difference (p1 ≠ p2)

Where:

- `p1` = conversion rate of control group (old pricing)
- `p2` = conversion rate of treatment group (new pricing)

---

## 📐 Choosing the Right Test: Z-Test vs T-Test

| Test Type      | When to Use                                                |
| -------------- | ---------------------------------------------------------- |
| **Z-Test**     | For large samples (n > 30) and known/approximated variance |
| **T-Test**     | For small samples (n < 30) or unknown population variance  |
| **Chi-Square** | For categorical outcomes in contingency tables             |

**✅ In this project:** We perform a **two-sample Z-test for proportions**, since:

- We're comparing conversion rates between 2 independent groups
- We have a large sample size (thousands of users)

---

## 🔍 Data Simulation & Structure

We simulate a dataset with \~10,000 users split into two groups:

- `group`: control or treatment
- `converted`: whether the user booked a flight (1) or not (0)

```python
import numpy as np
import pandas as pd

def simulate_ab_test(n=10000, p_control=0.12, p_treatment=0.135):
    n_control = n // 2
    n_treatment = n - n_control

    control_data = pd.DataFrame({
        'group': 'control',
        'converted': np.random.binomial(1, p_control, n_control)
    })
    treatment_data = pd.DataFrame({
        'group': 'treatment',
        'converted': np.random.binomial(1, p_treatment, n_treatment)
    })

    return pd.concat([control_data, treatment_data]).reset_index(drop=True)
```

---

## 📊 Statistical Hypothesis Test (Manual + Code)

### 1. Calculate Sample Stats

```python
p1 = control_data['converted'].mean()
p2 = treatment_data['converted'].mean()
n1 = len(control_data)
n2 = len(treatment_data)
```

### 2. Pooled Proportion & Standard Error

```python
p_pool = (control_data['converted'].sum() + treatment_data['converted'].sum()) / (n1 + n2)
se_pool = np.sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))
```

> **Why Pooled?** Under H₀, we assume both groups have the same conversion rate, so we use their combined average.

### 3. Z-Statistic

```python
z = (p2 - p1) / se_pool
```

### 4. P-value & Critical Value

```python
from scipy.stats import norm
z_crit = norm.ppf(1 - 0.05 / 2)  # for 95% confidence
p_val = 2 * (1 - norm.cdf(abs(z)))
```

### 5. Decision

- Reject H₀ if `|z| > z_crit` or `p < α` (usually 0.05)

---

## 📉 Visualization: Z-Test & Confidence Interval

```python
import matplotlib.pyplot as plt
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x)

plt.plot(x, y)
plt.axvline(z, color='red', label=f'Z = {z:.2f}')
plt.axvline(-z_crit, linestyle='--', color='gray')
plt.axvline(z_crit, linestyle='--', color='gray')
plt.fill_between(x, y, where=(x < -z_crit) | (x > z_crit), color='gray', alpha=0.2)
plt.title('Z-Test for Conversion Rate Difference')
plt.legend()
plt.show()
```

---

## 🎯 Confidence Intervals (CI) — Logic & Tradeoffs

> **CI = Observed Difference ± zₓ × Standard Error**

```python
diff = p2 - p1
se_diff = np.sqrt(p1*(1-p1)/n1 + p2*(1-p2)/n2)
z_star = norm.ppf(0.975)  # 95% CI
ci_lower = diff - z_star * se_diff
ci_upper = diff + z_star * se_diff
```

### 📌 Interpretation

- "We are 95% confident that the true uplift lies between CI\_lower and CI\_upper."
- If CI **excludes 0**, result is statistically significant.

### 🔁 Tradeoff

| CI Width  | Confidence Level | Variance         | Precision      |
| --------- | ---------------- | ---------------- | -------------- |
| Narrow CI | Low confidence   | Small            | High precision |
| Wide CI   | High confidence  | High (uncertain) | Less precise   |

> ✅ 95% CI is a balance: confident but not too wide.

> ❌ Your interpretation ("lower CI is better") is a common mistake. The **name 'confidence interval'** reflects how confident we are that the interval contains the true value — **not how tightly it hugs the mean**.

---

## 📈 Result Example (with Screenshot)



- Z = 2.45
- p-value = 0.014
- 95% CI = [0.0054, 0.0201]

> ✅ Conclusion: Statistically significant uplift detected from new pricing strategy.

---

