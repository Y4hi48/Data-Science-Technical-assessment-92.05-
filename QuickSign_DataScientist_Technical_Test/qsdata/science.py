"""Module containing some function for science processing."""

import numpy as np
from sklearn import metrics


def mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Compute mean squared error between two 1D arrays : y_true and y_true.

    Args:
        y_true: 1D numpy array containing floats
        y_pred: 1D numpy array containing floats

    Returns:
        mean squared error between y_true and y_pred

    Raises:
        ValueError if numpy arrays have more than one dimension.
    """
    if y_true.ndim != 1 or y_pred.ndim != 1:
        raise ValueError("Input arrays should be 1-dimensional.")

    if y_true.shape != y_pred.shape:
        raise ValueError("Input arrays should have the same shape.")

    # sklearn for precision
    return metrics.mean_squared_error(y_true, y_pred)


def moving_average(data: np.ndarray, window_size: int) -> np.ndarray:
    """Compute moving average of a 1D array data.

    Args:
        data: 1D numpy array containing floats

    Returns:
        numpy array containing moving average with the given window_size.

    Raises:
        ValueError if numpy arrays have more than one dimension.
    """
    if data.ndim != 1:
        raise ValueError("Input array should be 1-dimensional.")

    if not isinstance(window_size, int) or window_size < 1:
        raise ValueError("Window size should be a positive integer greater than 0.")

    if window_size > len(data):
        raise ValueError("Window size should not exceed the length of the data.")

    result = np.convolve(data, np.ones(window_size), 'valid') / window_size
    return result


def find_duplicates(arr: list[float]) -> list[float]:
    """Find duplicates in a list of floats.

    Args:
        arr: List of floats.

    Returns:
        List of duplicates found in the input list.

    Raises:
        ValueError: if input is not a list of floats or integers.
    """
    if not isinstance(arr, list):
        raise ValueError("Input should be a list.")
    if not all(isinstance(x, (float, int)) for x in arr):
        raise ValueError("Input should be a list of floats or integers.")

    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)


def prime_factors(n: int) -> list[int]:
    """Find all prime factors of a number n.

    Args:
        n: Integer number to find prime factors of.

    Returns:
        List of prime factors of n.

    Raises:
        ValueError: if input is not a positive integer.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input should be a positive integer.")

    factors = []
    factor = 2
    while n > 1:
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += 1

    return factors


def quicksort(arr: list[int]) -> list[int]:
    """Sort a list of integers using the quicksort algorithm.

    Args:
        arr: List of integers to be sorted

    Returns:
        A new list containing the sorted integers

    Raises:
        ValueError if the input is not a list of integers
    """
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")
    
    for element in arr:
        if not isinstance(element, int):
            raise ValueError("All elements in the list must be integers")

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)