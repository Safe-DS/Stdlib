import pytest
from safeds.data import SupervisedDataset
from safeds.data.tabular import Table
from safeds.exceptions import PredictionError
from safeds.ml.regression import RidgeRegression


def test_ridge_regression_predict() -> None:
    table = Table.from_csv("tests/resources/test_ridge_regression.csv")
    supervised_dataset = SupervisedDataset(table, "T")
    ridge_regression = RidgeRegression()
    ridge_regression.fit(supervised_dataset)
    ridge_regression.predict(supervised_dataset.feature_vectors)
    assert True  # This asserts that the predict method succeeds


def test_ridge_regression_predict_not_fitted() -> None:
    table = Table.from_csv("tests/resources/test_ridge_regression.csv")
    supervised_dataset = SupervisedDataset(table, "T")
    ridge_regression = RidgeRegression()
    with pytest.raises(PredictionError):
        ridge_regression.predict(supervised_dataset.feature_vectors)


def test_ridge_regression_predict_invalid() -> None:
    table = Table.from_csv("tests/resources/test_ridge_regression.csv")
    invalid_table = Table.from_csv("tests/resources/test_ridge_regression_invalid.csv")
    supervised_dataset = SupervisedDataset(table, "T")
    invalid_supervised_dataset = SupervisedDataset(invalid_table, "T")
    ridge_regression = RidgeRegression()
    ridge_regression.fit(supervised_dataset)
    with pytest.raises(PredictionError):
        ridge_regression.predict(invalid_supervised_dataset.feature_vectors)
