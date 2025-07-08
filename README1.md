# ✈️ A/B Testing Flight Booking Conversion Rates

> 🌟 A hands-on data science project simulating an A/B test to evaluate the impact of a new pricing strategy on booking conversions — inspired by real-world scenarios at Booking.com.

---

## 📌 Project Overview

Imagine your Flights team rolls out a **new pricing strategy** and wants to see if it boosts bookings. But how do you know the observed increase isn’t just random?

This project walks through **simulating** an A/B test, **applying hypothesis testing**, and **visualizing** the results to make informed decisions.

We simulate rich user interaction data with:

- Different flight routes
- Device types (mobile vs desktop)
- Time on page
- Booking behavior (`booked = 1 or 0`)

---

## 👥 Target Audience

This project is perfect for:

- Aspiring and current **Data Scientists**, **Analysts**, and **Product Managers**
- Anyone preparing for **data science interviews** involving experimentation
- Learners wanting a **conceptual + practical understanding** of hypothesis testing

---

## 🧪 Why Hypothesis Testing?

In A/B testing, we want to know:

> 🗨️ *Is the new version better — or is it just random noise?*

That’s where **hypothesis testing** comes in.

### 👇 In Simple Terms:

| Concept                         | Meaning                                                    |
| ------------------------------- | ---------------------------------------------------------- |
| **Null Hypothesis (H₀)**        | No difference between control & treatment                  |
| **Alternative Hypothesis (H₁)** | Treatment has a measurable effect                          |
| **Significance Level (α)**      | Maximum acceptable chance of false positive (usually 0.05) |
| **p-value**                     | Probability of observed effect if H₀ is true               |
| **Test Statistic (z or t)**     | How far your observed result is from the expected          |

We reject H₀ if the p-value is low (typically < 0.05), meaning the observed effect is unlikely due to chance.

---

## 📊 Choosing the Right Test

| 🧪 Test Type               | When to Use                                |
| -------------------------- | ------------------------------------------ |
| **Z-test for proportions** | ✅ Large sample, binary outcomes (our case) |
| **T-test**                 | Small sample, comparing means              |
| **Chi-square test**        | Count data in contingency tables           |

📌 For this project, we use a **two-sample Z-test for proportions** to compare conversion rates between control and treatment groups.

---

## 🐝 Simulated Dataset

We simulate 10,000 users with metadata:

```python
import pandas as pd
import numpy as np

def simulate_ab_test(n=10000, seed=42):
    np.random.seed(seed)
    
    df = pd.DataFrame({
        "user_id": np.arange(n),
        "group": np.random.choice(["control", "treatment"], size=n),
        "flight_route": np.random.choice(["AMS-JFK", "LHR-DXB", "CDG-SIN"], size=n),
        "device_type": np.random.choice(["mobile", "desktop"], size=n),
        "time_on_page": np.random.normal(45, 15, n).clip(5, 120),
    })

    def simulate_booking(row):
        base_rate = 0.06
        lift = 0.02 if row['group'] == 'treatment' else 0
        if row['device_type'] == 'mobile':
            lift += 0.01
        prob = base_rate + lift
        return np.random.rand() < prob

    df["booked"] = df.apply(simulate_booking, axis=1).astype(int)
    return df
```

> ✅ We simulate uplift due to treatment group and mobile device use.

---

## 📊 Hypothesis Testing Calculation (Z-Test)

```python
# Sample proportions
p1 = control_data['booked'].mean()
p2 = treatment_data['booked'].mean()

# Pooled proportion under H₀
p_pool = (control_data['booked'].sum() + treatment_data['booked'].sum()) / (n1 + n2)

# Standard error
se_pool = np.sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))

# Z-score
z = (p2 - p1) / se_pool

# P-value
from scipy.stats import norm
p_value = 2 * (1 - norm.cdf(abs(z)))

# Critical z-value
z_crit = norm.ppf(0.975)  # for 95% confidence
```

---

## 🔄 Visualizing Hypothesis Test

```python
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x)

plt.plot(x, y, label='Z-distribution')
plt.axvline(z, color='red', label=f'Z = {z:.2f}')
plt.axvline(-z_crit, linestyle='--', color='gray')
plt.axvline(z_crit, linestyle='--', color='gray')
plt.fill_between(x, y, where=(x < -z_crit) | (x > z_crit), color='gray', alpha=0.3)
plt.title("Two-Tailed Z-Test")
plt.legend()
plt.show()
```

---

## 🔢 Confidence Interval (CI)

```python
diff = p2 - p1
se_diff = np.sqrt(p1*(1-p1)/n1 + p2*(1-p2)/n2)
z_star = norm.ppf(0.975)  # 95% CI
ci_lower = diff - z_star * se_diff
ci_upper = diff + z_star * se_diff
```

> "We are 95% confident that the true uplift lies between **CI\_lower** and **CI\_upper**."

---