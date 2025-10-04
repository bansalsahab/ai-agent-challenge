import pandas as pd

from custom_parsers.icici_parser import parse


def test_parser_equals_sample():
    expected_df = pd.read_csv("data/icici/icici_sample.csv")
    result = parse(f"data/icici/icici_sample.pdf")
    assert list(result.columns) == list(expected_df.columns)
    assert result.equals(expected_df)
