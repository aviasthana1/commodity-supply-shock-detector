from __future__ import annotations

import pandas as pd


def event_window_pnl(returns: pd.Series, event_date: str, window: int = 5) -> float:
    idx = returns.index.astype(str)
    if event_date not in idx:
        return 0.0
    loc = list(idx).index(event_date)
    window_rets = returns.iloc[loc : loc + window]
    return float(window_rets.sum())
