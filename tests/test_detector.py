from commodity_supply_shock_detector.detector import SupplyShockDetector


def test_detector_runs() -> None:
    out = SupplyShockDetector().run()
    assert len(out) >= 1
