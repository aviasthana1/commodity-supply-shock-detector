from __future__ import annotations

import pandas as pd
from sklearn.ensemble import IsolationForest


class ReturnAnomalyDetector:
    def __init__(self, contamination: float = 0.05, random_state: int = 5) -> None:
        self.model = IsolationForest(contamination=contamination, random_state=random_state)
        self._fitted = False

    def fit_predict(self, returns: pd.DataFrame) -> pd.Series:
        x = returns.dropna().values
        pred = self.model.fit_predict(x)
        labels = pd.Series(pred, index=returns.dropna().index, name="anomaly")
        self._fitted = True
        return labels
