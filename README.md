# 📊 Copper Probabilistic Forecasting Engine

## From Real Scrap Copper to Probabilistic Decision Modeling

This project started from a real-world situation.

After major home maintenance, we ended up with a large bulk of old copper wiring — nearly 20 years of cables collected from walls, storage, and replaced systems.

While trying to sell it on Facebook Marketplace, I noticed something:

Prices were fluctuating daily.

Different buyers. Different quotes. Different numbers.

That raised a serious question:

Should I sell now… or wait?

Instead of relying on opinions or headlines, I decided to model the probabilities.

This repository contains a probabilistic forecasting engine that simulates potential future copper outcomes across multiple time horizons.

---

## 🎯 What This Engine Does

This engine does NOT predict a single price.

It estimates:

- Expected return over 1M, 3M, 6M, 1Y
- Volatility of possible outcomes
- Probability of positive return
- Probability of significant downside
- Probability of strong upside

It converts uncertainty into structured decision-relevant probabilities.

---

## 🧠 Market Research & Statistical Approach

This project reflects a market research mindset:

- Observing price fluctuations in real marketplaces
- Recognizing macroeconomic drivers (global copper + USD/EGP)
- Identifying volatility patterns
- Structuring uncertainty into measurable outcomes

Statistically, the engine uses:

- Log returns (instead of naïve percentage change)
- Student-t distribution to model fat-tail risk
- Monte Carlo simulation (10,000+ paths)
- Correlation analysis across time frequencies
- Volatility-adjusted dynamic thresholds

It combines global copper futures with USD/EGP exchange rate to approximate local Egyptian copper value exposure.

---

## 🔬 Why It Is Different

Unlike simple trend extrapolation:

- It models heavy-tail market risk.
- It estimates degrees of freedom directly from historical data.
- It uses monthly correlation (not noisy daily correlation).
- It avoids arbitrary decision rules by using volatility-based thresholds.

It is built from statistical reasoning, not price guessing.

---

## 🤖 About the Code

The statistical framework, modeling logic, and methodology were designed by me.

The Python implementation was developed with assistance from ChatGPT, which I used as a coding support tool to translate statistical logic into executable Python.

This project demonstrates:

- Applied statistical reasoning
- Market research thinking
- Correlation analysis across time horizons
- Decision science under uncertainty
- Structured use of AI tools in model implementation

---

## 🛠 How To Run

Install dependencies:

py -m pip install yfinance numpy pandas scipy

Run the engine:

py copper_engine.py

The script automatically downloads data, estimates parameters, runs simulations, and prints probability-based outputs.

---

## 📘 Full Technical Explanation

For a detailed breakdown of:

- Log return mathematics
- Student-t modeling
- Monte Carlo methodology
- Correlation frequency selection
- Volatility-based threshold design

See:

DETAILED_MODEL_EXPLANATION.md

---

## 👤 Author

Investment & Finance Graduate  
Market Research & Analytics Focused  
Prompt Engineer & LLM Trainer (Outlier / Toloka AI)  

Interested in probabilistic reasoning, structured decision-making, and applied quantitative modeling.

