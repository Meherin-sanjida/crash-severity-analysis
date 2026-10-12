import pandas as pd
import pytest


def validate_columns(df):
    required = {'CrashSeverity', 'SpeedLimit'}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f'Missing required columns: {sorted(missing)}')


def prepare_data(df):
    validate_columns(df)
    result = df.copy()
    result['SpeedLimit'] = pd.to_numeric(result['SpeedLimit'], errors='coerce')
    result['CrashSeverity'] = result['CrashSeverity'].astype('string').str.strip()
    valid = (result['SpeedLimit'].notna() & (result['SpeedLimit'] > 0)
             & result['CrashSeverity'].notna() & result['CrashSeverity'].ne(''))
    return result.loc[valid].copy()


def severity_counts(df):
    return df['CrashSeverity'].value_counts().sort_index()


def severity_by_speed(df):
    return pd.crosstab(df['SpeedLimit'], df['CrashSeverity'])


def test_required_columns():
    with pytest.raises(ValueError, match='Missing required columns'):
        prepare_data(pd.DataFrame({'SpeedLimit': [30]}))


def test_valid_rows_retained():
    df = pd.DataFrame({'CrashSeverity': ['A', 'B'], 'SpeedLimit': [30, 45]})
    assert len(prepare_data(df)) == 2


def test_invalid_rows_excluded():
    df = pd.DataFrame({'CrashSeverity': ['A', None, ' ', 'B', 'C'],
                       'SpeedLimit': [30, 45, 25, -5, 'unknown']})
    assert len(prepare_data(df)) == 1


def test_numeric_string_speed():
    df = pd.DataFrame({'CrashSeverity': ['A'], 'SpeedLimit': ['35']})
    assert prepare_data(df)['SpeedLimit'].iloc[0] == 35


def test_severity_counts():
    df = pd.DataFrame({'CrashSeverity': ['A', 'B', 'A']})
    assert severity_counts(df).to_dict() == {'A': 2, 'B': 1}


def test_cross_tabulation():
    df = pd.DataFrame({'CrashSeverity': ['A', 'B', 'A'],
                       'SpeedLimit': [30, 30, 45]})
    table = severity_by_speed(df)
    assert table.loc[30, 'A'] == 1
    assert table.loc[30, 'B'] == 1
    assert table.loc[45, 'A'] == 1


def test_summary_totals():
    df = pd.DataFrame({'CrashSeverity': ['A', 'B', 'A'],
                       'SpeedLimit': [30, 30, 45]})
    assert severity_counts(df).sum() == len(df)
    assert severity_by_speed(df).to_numpy().sum() == len(df)


def test_empty_valid_data():
    df = pd.DataFrame({'CrashSeverity': [None], 'SpeedLimit': [-1]})
    assert prepare_data(df).empty


def test_original_data_unchanged():
    df = pd.DataFrame({'CrashSeverity': [' A '], 'SpeedLimit': ['30']})
    prepare_data(df)
    assert df.loc[0, 'CrashSeverity'] == ' A '
    assert df.loc[0, 'SpeedLimit'] == '30'
