from safeds.data import SupervisedDataset
from safeds.data.tabular import Table


def test_supervised_dataset_target_values() -> None:
    table = Table.from_csv("tests/resources/test_supervised_dataset.csv")
    supervised_dataset = SupervisedDataset(table, "T")
    assert supervised_dataset.target_values._data[0] == 0
    assert supervised_dataset.target_values._data[1] == 1
