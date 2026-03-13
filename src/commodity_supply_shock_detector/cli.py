from commodity_supply_shock_detector.detector import SupplyShockDetector


def main() -> None:
    for line in SupplyShockDetector().run():
        print(line)


if __name__ == "__main__":
    main()
