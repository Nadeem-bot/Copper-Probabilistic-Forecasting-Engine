import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import norm, t

N_SIM = 10000
LOOKBACK_YEARS = 5
K = 0.5

HORIZONS = {
    "1M": 21,
    "3M": 63,
    "6M": 126,
    "1Y": 252
}

def download_prices():
    copper = yf.download("HG=F", period=f"{LOOKBACK_YEARS}y", auto_adjust=False)
    fx = yf.download("EGP=X", period=f"{LOOKBACK_YEARS}y", auto_adjust=False)

    copper_price = copper["Close"]
    fx_price = fx["Close"]

    df = pd.concat([copper_price, fx_price], axis=1)
    df.columns = ["Copper", "FX"]
    df.dropna(inplace=True)
    return df


def compute_log_returns(prices):
    return np.log(prices / prices.shift(1)).dropna()


def compute_monthly_correlation(prices):
    monthly_prices = prices.resample("ME").last()
    monthly_lr = compute_log_returns(monthly_prices)
    return monthly_lr["Copper"].corr(monthly_lr["FX"])


def fit_nu(x):
    df_hat, _, _ = t.fit(x)
    return max(3.5, min(50.0, df_hat))


def t_scale(nu):
    return np.sqrt((nu - 2.0) / nu)


def simulate(mu, sigma, corr, nu_c, nu_f, days):

    corr = np.clip(corr, -0.999, 0.999)
    R = np.array([[1.0, corr], [corr, 1.0]])
    L = np.linalg.cholesky(R)

    z = np.random.normal(size=(N_SIM, days, 2))
    z_corr = z @ L.T

    u = norm.cdf(z_corr)

    shock_c = t.ppf(u[:, :, 0], df=nu_c)
    shock_f = t.ppf(u[:, :, 1], df=nu_f)

    shock_c *= t_scale(nu_c)
    shock_f *= t_scale(nu_f)

    r_c = mu[0] + sigma[0] * shock_c
    r_f = mu[1] + sigma[1] * shock_f

    sum_c = r_c.sum(axis=1)
    sum_f = r_f.sum(axis=1)

    return np.exp(sum_c + sum_f) - 1


def main():

    print("Downloading data...")
    prices = download_prices()

    daily_lr = compute_log_returns(prices)

    mu = daily_lr.mean().values
    sigma = daily_lr.std().values

    monthly_corr = compute_monthly_correlation(prices)

    nu_c = fit_nu(daily_lr["Copper"].values)
    nu_f = fit_nu(daily_lr["FX"].values)

    print(f"\nUsing Monthly Correlation: {monthly_corr:.4f}")
    print(f"Estimated nu Copper: {nu_c:.2f}")
    print(f"Estimated nu FX: {nu_f:.2f}\n")

    for label, days in HORIZONS.items():

        sim_returns = simulate(mu, sigma, monthly_corr, nu_c, nu_f, days)

        sigma_T = np.std(sim_returns)
        dip_threshold = -K * sigma_T
        win_threshold = K * sigma_T

        print("="*60)
        print(f"Horizon: {label}")
        print(f"Expected Return: {np.mean(sim_returns):.2%}")
        print(f"Volatility: {sigma_T:.2%}")
        print(f"P(Return > 0): {np.mean(sim_returns > 0):.2%}")
        print(f"P(Dip): {np.mean(sim_returns <= dip_threshold):.2%}")
        print(f"P(Win): {np.mean(sim_returns >= win_threshold):.2%}")
        print("="*60)

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
