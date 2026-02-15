# Copper-Probabilistic-Forecasting-Engine

A beginner-friendly Python tool that uses historical data + Monte Carlo simulation to estimate the probability of winning or dipping when holding copper over multiple horizons.

This project models:
- Global copper price (Yahoo Finance symbol: `HG=F`)
- USD/EGP exchange rate (Yahoo Finance symbol: `EGP=X`)
- Multi-horizon outcomes: **1M, 3M, 6M, 1Y**
- Fat-tail risk using **Student-t distribution**
- Dependence using **correlation** (optionally computed at monthly frequency)

> ⚠️ Important: This is a probabilistic decision-support tool, not a guarantee of profit.

---

## What You Need

- Windows 10/11
- Python installed (you can use `py` on Windows)
- Internet connection (to download data)

---

## 1) Install Python (if needed)

Open **CMD** and run:

```bat
py --version
