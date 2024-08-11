import pytest

from qsdata.data_processing import (
    aggregate_data,
    complex_filter,
    filter_data,
    sort_data,
)


@pytest.fixture
def sample_data():
    return [
        {"name": "Alice", "age": 30, "city": "Paris"},
        {"name": "Bob", "age": 25, "city": "Paris"},
        {"name": "Charlie", "age": 35, "city": "London"},
        {"name": "David", "age": 40, "city": "New York"},
        {"name": "Eve", "age": 22, "city": "Paris"},
    ]


def test_filter_data(sample_data):
    result = filter_data(sample_data, "city", "Paris")
    assert len(result) == 3
    assert all(item["city"] == "Paris" for item in result)
    assert not filter_data(sample_data, 1, "city")


def test_sort_data(sample_data):
    result = sort_data(sample_data, "age")
    assert result[0]["age"] == 22
    assert result[-1]["age"] == 40
    with pytest.raises(KeyError):
        sort_data(sample_data, "country")


def test_complex_filter(sample_data):
    result = complex_filter(sample_data, "age", 30)
    assert len(result) == 2
    assert all(item["age"] > 30 for item in result)
    with pytest.raises(ValueError):
        complex_filter(sample_data, "city", "Paris")


def test_aggregate_data(sample_data):
    result = aggregate_data(sample_data, "city")
    assert result == {"Paris": 3, "London": 1, "New York": 1}
    with pytest.raises(KeyError):
        aggregate_data(sample_data, "London")
