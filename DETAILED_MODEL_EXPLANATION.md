# 📘 Detailed Model Explanation

## 1. Real-World Motivation

This project originated from a real decision problem.

After home maintenance, a large quantity of copper wiring was extracted from the house. While attempting to sell it locally, daily buyer quotes fluctuated noticeably.

Instead of relying on opinions or guessing direction, I asked:

How can I quantify the probability of future price outcomes?

This reflects a market research mindset:

- Observe real-world behavior
- Identify structural drivers
- Translate noise into measurable variables
- Convert uncertainty into probability distributions

This project is the statistical translation of that thinking.

---

# 2. Data Structure

The model uses two time series:

1) Copper Futures Price (HG=F)
2) USD/EGP Exchange Rate (EGP=X)

Why both?

Because local copper exposure in Egypt depends on:

Local Value ≈ Global Copper × USD/EGP

So if:

C_t = copper price at time t
F_t = USD/EGP rate at time t

Then effective local exposure is influenced by both.

---

# 3. Log Returns (Core Mathematical Foundation)

Instead of percentage return:

Percentage Return:
R_t = (P_t - P_{t-1}) / P_{t-1}

We use log returns:

r_t = ln(P_t / P_{t-1})

Why?

Because log returns have three critical properties:

1) Time Additivity
If:
r1 = ln(P1/P0)
r2 = ln(P2/P1)

Then total log return:

r_total = r1 + r2

Which equals:

ln(P2/P0)

This is mathematically consistent.

2) Proper Compounding
Total return across T periods:

Total Return = exp(Σ r_t) - 1

3) Statistical Stability
Log returns are more symmetric and stable for modeling.

---

# 4. Mean and Volatility Estimation

From historical log returns:

Let r_t be daily log returns.

Mean:

μ = (1/n) Σ r_t

Standard deviation (volatility):

σ = sqrt( (1/(n-1)) Σ (r_t - μ)^2 )

Interpretation:

μ = average daily growth rate (log scale)
σ = daily uncertainty level

---

# 5. Why Not Normal Distribution?

If returns were normally distributed:

r_t ~ N(μ, σ²)

Then extreme moves would be rare.

But financial markets exhibit fat tails.

This means:

Extreme outcomes occur more frequently than normal distribution predicts.

So instead of normal distribution:

We use Student-t distribution.

---

# 6. Student-t Distribution

The Student-t distribution has parameter ν (degrees of freedom).

Notation:

r_t ~ t(ν)

Properties:

If ν → ∞ → distribution approaches normal.

If ν is small → fatter tails.

Variance of t-distribution:

Var = ν / (ν - 2)   (for ν > 2)

In simulation, shocks are scaled to preserve volatility:

Adjusted Shock = t_shock × sqrt((ν - 2) / ν)

This ensures simulated variance matches historical variance.

This allows realistic modeling of extreme upside and downside.

---

# 7. Correlation Modeling

Let:

r_c,t = copper log return
r_f,t = FX log return

Correlation coefficient:

ρ = Cov(r_c, r_f) / (σ_c × σ_f)

Where:

Cov(r_c, r_f) = (1/(n-1)) Σ (r_c,t - μ_c)(r_f,t - μ_f)

The model estimates correlation across:

- Daily
- Weekly
- Monthly
- Quarterly
- Yearly

Monthly correlation is selected for simulation because:

- Daily contains noise
- Monthly captures macro-level structure

This is a research-based modeling decision.

---

# 8. Monte Carlo Simulation

Monte Carlo simulation generates possible future scenarios.

Steps:

1) Generate random shocks
2) Impose correlation structure
3) Apply Student-t transformation
4) Scale by historical volatility
5) Add mean drift
6) Aggregate over time

Mathematically:

For each simulation path i and day t:

r_c,t = μ_c + σ_c × ε_c,t
r_f,t = μ_f + σ_f × ε_f,t

Where:

ε ~ correlated Student-t distribution

Aggregate over T days:

R_total = exp( Σ (r_c,t + r_f,t) ) - 1

This produces one simulated outcome.

Repeat 10,000 times → full distribution.

---

# 9. Distribution of Outcomes

From simulations we obtain:

Mean:

E[R]

Volatility:

σ_T = std(simulated_returns)

Probability of profit:

P(R > 0)

Probability of significant dip:

P(R ≤ -0.5 × σ_T)

Probability of strong upside:

P(R ≥ 0.5 × σ_T)

These probabilities form structured decision inputs.

---

# 10. Volatility-Based Threshold Design

Instead of fixed thresholds:

Threshold = ± k × σ_T

Where:

k = 0.5 in this model

This means:

If volatility increases → thresholds widen.
If volatility decreases → thresholds narrow.

This keeps decision logic adaptive.

---

# 11. Market Research Interpretation Layer

This is not just statistics.

This is applied market research thinking:

- Identify macro drivers (global demand, USD strength)
- Test structural relationships (correlation frequency)
- Quantify uncertainty
- Convert statistical output into decision relevance

This bridges quantitative modeling with economic reasoning.

---

# 12. Role of ChatGPT

The statistical logic, modeling design, and structure were conceptualized and structured by me.

ChatGPT was used as:

- A coding assistant
- A translation tool from statistical logic to Python
- A debugging helper

This project demonstrates structured use of AI tools in quantitative implementation.

---

# 13. What This Project Shows About My Skillset

This project demonstrates:

- Understanding of log-return mathematics
- Awareness of distribution assumptions
- Heavy-tail risk modeling
- Correlation frequency sensitivity
- Monte Carlo simulation mechanics
- Volatility-adjusted decision thresholds
- Market research reasoning applied to real data

It is not a black-box model.

It is a structured probabilistic framework built from first principles.

