# pylint: disable=pointless-statement

import pandas as pd
import pytest
from safe_ds.data import Table
from safe_ds.exceptions import ColumnNameError


# noinspection PyStatementEffect
def test_getitem_invalid():
    with pytest.raises(ColumnNameError):
        table = Table(pd.DataFrame(data={"col1": [1], "col2": [2]}))
        row = table.get_row(0)
        row["col3"]


def test_getitem_valid():
    table = Table(pd.DataFrame(data={"col1": [1], "col2": [2]}))
    row = table.get_row(0)
    assert row["col1"] == 1 and row["col2"] == 2