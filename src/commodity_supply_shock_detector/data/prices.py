from __future__ import annotations

import numpy as np
import pandas as pd


def synthetic_commodity_returns(n: int = 300, seed: int = 5) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    idx = pd.bdate_range("2025-06-02", periods=n)
    syms = ["CL", "NG", "HG", "ZW"]
    data = {}
    for s in syms:
        r = 0.0002 + 0.018 * rng.standard_normal(n)
        if s == "CL":
            r[120] += 0.08
        if s == "NG":
            r[180] += 0.12
        data[s] = r
    return pd.DataFrame(data, index=idx)
