SUPPLY_KEYWORDS = {"outage", "strike", "disrupt", "cut", "surge", "drought", "shortage"}


def news_supply_score(headline: str) -> float:
    tokens = set(headline.lower().split())
    hits = len(tokens & SUPPLY_KEYWORDS)
    return min(1.0, hits / 3)
