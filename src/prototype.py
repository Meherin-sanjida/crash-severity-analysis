from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from data_processing import clean_crash_data, load_crash_data

DATA_FILE = Path("data/right_turn_crashes.csv")
RESULTS_DIR = Path("results")


def main():
    RESULTS_DIR.mkdir(exist_ok=True)

    print("Loading crash data...")

    df = load_crash_data(DATA_FILE)

    print(f"Original number of records: {len(df)}")

    df = clean_crash_data(df)

    print(f"Records after cleaning: {len(df)}")

    print("\nDataset columns:")
    print(df.columns.tolist())

    print("\nCrash severity distribution:")
    print(df["CrashSeverity"].value_counts())

    # Create a cross-tabulation of speed limit and crash severity
    print("\nSpeed limit distribution by crash severity:")

    speed_summary = pd.crosstab(
        df["CrashSeverity"],
        df["SpeedLimit"]
    )

    print(speed_summary)

    # Save summary table
    speed_summary.to_csv(
        RESULTS_DIR / "prototype_summary.csv"
    )

    # Create crash-severity figure
    severity_counts = df["CrashSeverity"].value_counts()

    severity_counts.plot(kind="bar")

    plt.xlabel("Crash Severity")
    plt.ylabel("Number of Crashes")
    plt.title("Distribution of Right-Turn Crash Severity")
    plt.tight_layout()

    plt.savefig(
        RESULTS_DIR / "severity_distribution.png",
        dpi=300
    )

    plt.close()

    print("\nPrototype completed successfully.")


if __name__ == "__main__":
    main()