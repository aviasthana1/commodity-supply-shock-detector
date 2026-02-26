from __future__ import annotations


def shock_score(news: float, vol_z: float, anomaly: int) -> float:
    base = 0.5 * news + 0.3 * min(abs(vol_z) / 3, 1.0)
    if anomaly == -1:
        base += 0.2
    return min(1.0, base)
