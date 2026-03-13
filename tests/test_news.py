from commodity_supply_shock_detector.features.news_hits import news_supply_score


def test_supply_keywords() -> None:
    assert news_supply_score("Pipeline outage cuts flows") >= 0.3
