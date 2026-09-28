import pandas as pd


def load_crash_data(filepath):
    """loads the crash dataset from a CSV file"""
    return pd.read_csv(filepath)


def clean_crash_data(df):
    """perform basic cleaning for the prototype"""
    df = df.copy()

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Remove exact duplicate rows
    df = df.drop_duplicates()

    return df


def get_severity_counts(df, severity_column):
    """returns counts for each crash severity category"""
    return (
        df[severity_column]
        .value_counts(dropna=False)
        .reset_index()
    )