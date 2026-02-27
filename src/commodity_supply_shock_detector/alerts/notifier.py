from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ShockAlert:
    date: str
    commodity: str
    score: float
    headline: str | None = None


def format_alert(alert: ShockAlert) -> str:
    h = f" — {alert.headline}" if alert.headline else ""
    return f"[{alert.date}] {alert.commodity} shock={alert.score:.2f}{h}"
