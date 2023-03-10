import pytest
from safeds.data import SupervisedDataset
from safeds.data.tabular import Table
from safeds.exceptions import PredictionError
from safeds.ml.regression import LinearRegression


def test_linear_regression_predict() -> None:
    table = Table.from_csv("tests/resources/test_linear_regression.csv")
    supervised_dataset = SupervisedDataset(table, "T")
    linear_regression = LinearRegression()
    linear_regression.fit(supervised_dataset)
    linear_regression.predict(supervised_dataset.feature_vectors)
    assert True  # This asserts that the predict method succeeds


def test_linear_regression_predict_not_fitted() -> None:
    table = Table.from_csv("tests/resources/test_linear_regression.csv")
    supervised_dataset = SupervisedDataset(table, "T")
    linear_regression = LinearRegression()
    with pytest.raises(PredictionError):
        linear_regression.predict(supervised_dataset.feature_vectors)


def test_linear_regression_predict_invalid() -> None:
    table = Table.from_csv("tests/resources/test_linear_regression.csv")
    invalid_table = Table.from_csv("tests/resources/test_linear_regression_invalid.csv")
    supervised_dataset = SupervisedDataset(table, "T")
    invalid_supervised_dataset = SupervisedDataset(invalid_table, "T")
    linear_regression = LinearRegression()
    linear_regression.fit(supervised_dataset)
    with pytest.raises(PredictionError):
        linear_regression.predict(invalid_supervised_dataset.feature_vectors)
