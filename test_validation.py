"""Automated tests for categorical right-turn crash severity validation"""

import pandas as pd
import pytest

SPEED_CATEGORIES = [
    "25 mph or less",
    "30 or 35 mph",
    "40 mph or more",
]
SEVERITY_CATEGORIES = ["Injury", "No injury"]


def prepare_data(df):
    """Keep observations with recognized speed and severity categories."""
    required = {"SpeedLimit", "CrashSeverity"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    clean = df.copy()
    for column in ("SpeedLimit", "CrashSeverity"):
        clean[column] = clean[column].astype("string").str.strip()

    valid = (
        clean["SpeedLimit"].isin(SPEED_CATEGORIES)
        & clean["CrashSeverity"].isin(SEVERITY_CATEGORIES)
    )
    return clean.loc[valid].copy()


def severity_counts(clean):
    return clean["CrashSeverity"].value_counts().reindex(
        SEVERITY_CATEGORIES, fill_value=0
    )


def severity_by_speed(clean):
    return pd.crosstab(
        clean["SpeedLimit"], clean["CrashSeverity"]
    ).reindex(
        index=SPEED_CATEGORIES,
        columns=SEVERITY_CATEGORIES,
        fill_value=0,
    )


@pytest.fixture
def sample_data():
    return pd.DataFrame(
        {
            "SpeedLimit": [
                "25 mph or less", "30 or 35 mph", "40 mph or more",
                "25 mph or less", None, "Unknown", " 30 or 35 mph ",
            ],
            "CrashSeverity": [
                "Injury", "No injury", "Injury", "No injury",
                "Injury", "Injury", " Injury ",
            ],
        }
    )


def test_required_columns(sample_data):
    with pytest.raises(ValueError, match="Missing required columns"):
        prepare_data(sample_data.drop(columns="SpeedLimit"))


def test_valid_rows_retained(sample_data):
    assert len(prepare_data(sample_data)) == 5


def test_invalid_rows_excluded(sample_data):
    clean = prepare_data(sample_data)
    assert clean["SpeedLimit"].isin(SPEED_CATEGORIES).all()
    assert clean["CrashSeverity"].isin(SEVERITY_CATEGORIES).all()


def test_whitespace_is_removed(sample_data):
    clean = prepare_data(sample_data)
    assert clean.iloc[-1]["SpeedLimit"] == "30 or 35 mph"
    assert clean.iloc[-1]["CrashSeverity"] == "Injury"


def test_severity_counts(sample_data):
    counts = severity_counts(prepare_data(sample_data))
    assert counts["Injury"] == 3
    assert counts["No injury"] == 2


def test_cross_tabulation(sample_data):
    table = severity_by_speed(prepare_data(sample_data))
    assert table.loc["25 mph or less", "Injury"] == 1
    assert table.loc["25 mph or less", "No injury"] == 1
    assert table.loc["30 or 35 mph", "Injury"] == 1
    assert table.loc["40 mph or more", "Injury"] == 1


def test_summary_totals(sample_data):
    clean = prepare_data(sample_data)
    assert severity_counts(clean).sum() == len(clean)
    assert severity_by_speed(clean).to_numpy().sum() == len(clean)


def test_empty_valid_data():
    invalid = pd.DataFrame(
        {"SpeedLimit": [None, "Unknown"], "CrashSeverity": ["Injury", None]}
    )
    clean = prepare_data(invalid)
    assert clean.empty
    assert severity_by_speed(clean).to_numpy().sum() == 0


def test_original_data_unchanged(sample_data):
    before = sample_data.copy(deep=True)
    prepare_data(sample_data)
    pd.testing.assert_frame_equal(sample_data, before)
