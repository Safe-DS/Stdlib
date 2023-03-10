import pandas as pd
import pytest
from safeds.data.tabular import Table
from safeds.data.tabular.transformation import LabelEncoder
from safeds.exceptions import NotFittedError


def test_inverse_transform_valid() -> None:
    test_table = Table(
        pd.DataFrame({"cities": ["paris", "paris", "tokyo", "amsterdam"]})
    )
    le = LabelEncoder()
    test_table = le.fit_transform(test_table, ["cities"])
    test_table = le.inverse_transform(test_table, "cities")
    assert test_table.schema.has_column("cities")
    assert test_table.to_columns()[0].get_value(0) == "paris"
    assert test_table.to_columns()[0].get_value(2) == "tokyo"
    assert test_table.to_columns()[0].get_value(3) == "amsterdam"


def test_inverse_transform_invalid() -> None:
    test_table = Table(
        pd.DataFrame({"cities": ["paris", "paris", "tokyo", "amsterdam"]})
    )
    le = LabelEncoder()
    # le.fit(test_table) removed to force NotFittedError
    with pytest.raises(NotFittedError):
        le.inverse_transform(test_table, "cities")
