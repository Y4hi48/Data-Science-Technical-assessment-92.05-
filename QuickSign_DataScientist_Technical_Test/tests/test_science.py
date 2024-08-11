import numpy as np
import pytest

from qsdata.science import (
    find_duplicates,
    mean_squared_error,
    moving_average,
    prime_factors,
    quicksort,
)


def test_prime_factors():
    assert prime_factors(28) == [2, 2, 7]
    assert prime_factors(29) == [29]
    with pytest.raises(ValueError):
        prime_factors(-20)


def test_mean_squared_error():
    y_true = np.array([1, 2, 3])
    y_pred = np.array([1, 2, 3])
    assert mean_squared_error(y_true, y_pred) == 0

    y_pred = np.array([2, 2, 2])
    assert mean_squared_error(y_true, y_pred) == 2 / 3
    with pytest.raises(ValueError):
        mean_squared_error(y_true, np.zeros((2, 4)))
    with pytest.raises(ValueError):
        mean_squared_error(np.zeros((2, 4)), y_pred)


def test_moving_average():
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    result = moving_average(data, 3)
    expected = np.array([2, 3, 4, 5, 6, 7, 8, 9])
    assert np.allclose(result, expected)


def test_find_duplicates():
    arr = [1, 2, 3, 1, 2, 4]
    duplicates = find_duplicates(arr)
    assert 1 in duplicates
    assert 2 in duplicates

    arr = [1, 2, 3, 4, 5]
    assert not find_duplicates(arr)


def test_quicksort():
    assert quicksort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]
    assert quicksort([]) == []
    assert quicksort([1]) == [1]
