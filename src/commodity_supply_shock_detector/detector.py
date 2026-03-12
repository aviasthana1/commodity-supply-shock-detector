from __future__ import annotations

import pandas as pd

from commodity_supply_shock_detector.alerts.notifier import ShockAlert, format_alert
from commodity_supply_shock_detector.data.events import SUPPLY_EVENTS
from commodity_supply_shock_detector.data.prices import synthetic_commodity_returns
from commodity_supply_shock_detector.features.news_hits import news_supply_score
from commodity_supply_shock_detector.features.vol_anomaly import return_vol_zscore
from commodity_supply_shock_detector.models.anomaly import ReturnAnomalyDetector
from commodity_supply_shock_detector.models.scorer import shock_score


class SupplyShockDetector:
    def __init__(self, vol_z_threshold: float = 2.5, news_threshold: float = 0.6) -> None:
        self.vol_z_threshold = vol_z_threshold
        self.news_threshold = news_threshold

    def scan_events(self) -> list[ShockAlert]:
        alerts: list[ShockAlert] = []
        for ev in SUPPLY_EVENTS:
            score = news_supply_score(ev["headline"])
            if score >= self.news_threshold:
                alerts.append(ShockAlert(ev["date"], ev["commodity"], score, ev["headline"]))
        return alerts

    def scan_prices(self, returns: pd.DataFrame | None = None) -> pd.DataFrame:
        rets = returns if returns is not None else synthetic_commodity_returns()
        anom = ReturnAnomalyDetector().fit_predict(rets)
        rows = []
        for col in rets.columns:
            vol_z = return_vol_zscore(rets[col])
            for dt in rets.index:
                vz = float(vol_z.get(dt, 0) or 0)
                an = int(anom.get(dt, 1))
                sc = shock_score(0.0, vz, an)
                if abs(vz) >= self.vol_z_threshold or an == -1:
                    rows.append({"date": str(dt.date()), "commodity": col, "vol_z": vz, "score": sc})
        return pd.DataFrame(rows)

    def run(self) -> list[str]:
        msgs = [format_alert(a) for a in self.scan_events()]
        price_hits = self.scan_prices()
        for _, row in price_hits.head(5).iterrows():
            msgs.append(f"[{row['date']}] {row['commodity']} vol_z={row['vol_z']:.2f} score={row['score']:.2f}")
        return msgs
