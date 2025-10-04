import os
from pathlib import Path

import pandas as pd

from agent import infer_schema, generate_parser_code


def test_infer_schema_matches_csv():
    repo_root = Path.cwd()
    csv_path = repo_root / "data" / "icici" / "icici_sample.csv"
    assert csv_path.exists()
    cols, dtypes = infer_schema(csv_path)
    expected = list(pd.read_csv(csv_path).columns)
    assert cols == expected


def test_generate_parser_code_contains_parse():
    cols = ["Date", "Description", "Debit Amt"]
    dtypes = {"Date": "date", "Description": "str", "Debit Amt": "float"}
    code = generate_parser_code("icici", cols, dtypes)
    assert isinstance(code, str) and len(code) > 0
    assert "def parse(" in code
