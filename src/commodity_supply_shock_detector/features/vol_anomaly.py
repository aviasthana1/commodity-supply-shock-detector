from __future__ import annotations

import pandas as pd


def return_vol_zscore(returns: pd.Series, window: int = 21) -> pd.Series:
    vol = returns.rolling(window).std()
    mu = vol.rolling(window * 2).mean()
    sd = vol.rolling(window * 2).std()
    return (vol - mu) / sd
