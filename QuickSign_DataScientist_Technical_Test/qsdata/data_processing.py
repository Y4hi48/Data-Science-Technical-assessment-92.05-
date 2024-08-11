from typing import Union, Dict, List

"""Module containing data processing for dicts."""

def filter_data(
    data: List[Dict[str, Union[int, str]]], key: Union[str, int], value: Union[int, str]
) -> List[Dict[str, Union[int, str]]]:
    """Filter data to keep only the items where data[key] == value.

    Args:
        data: The list of data to filter.
        key: The key to filter by.
        value: The value to match.

    Returns:
        A list of dictionaries that match the filter criteria.

    Raises:
        ValueError: if data is not a list of dictionaries.
        ValueError: if key is not a string or int.
        ValueError: if value is not an int or a string.
    """
    if not isinstance(data, list):
        raise ValueError("data should be a list.")
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("data should be a list of dictionaries.")
    if not isinstance(key, (str, int)):
        raise ValueError("key should be a string or int.")
    if not isinstance(value, (int, str)):
        raise ValueError("value should be an int or a string.")

    return [item for item in data if item.get(key) == value]

def sort_data(
    data: List[Dict[str, Union[int, str]]], key: str
) -> List[Dict[str, Union[int, str]]]:
    """Sort data by a given key in ascending order.

    Args:
        data: The list of data to sort.
        key: The key to sort by.

    Returns:
        A list of dictionaries sorted by the specified key.
        If the values of dictionary are strings, they are sorted in lexicographical order.

    Raises:
        ValueError: if data is not a list of dictionaries.
        ValueError: if key is not a string.
        KeyError: if key is not found in a dictionary.
        ValueError: if the values of dictionary are not uniform in type.
    """
    if not isinstance(data, list):
        raise ValueError("data should be a list.")
    if not isinstance(key, str):
        raise ValueError("key should be a string.")

    # Ensure all items are dictionaries and the key exists
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("data should be a list of dictionaries.")
        if key not in item:
            raise KeyError(f"Key {key} not found in dictionary.")
    
    # Check that all values are of the same type
    first_type = type(data[0][key])
    if not all(isinstance(item[key], first_type) for item in data):
        raise ValueError("Values of dictionary should be uniform in type.")
        
    return sorted(data, key=lambda dic: dic[key])

def complex_filter(
    data: List[Dict[str, Union[int, str]]], key: str, threshold: int
) -> List[Dict[str, Union[int, str]]]:
    """Filter data using a threshold condition.

    Args:
        data: The list of data to filter.
        key: The key to filter by.
        threshold: The threshold value.

    Returns:
        A list of dictionaries that match the threshold criteria.

    Raises:
        ValueError: if data is not a list of dictionaries.
        ValueError: if key is not a string.
        ValueError: if threshold is not an int.
    """
    if not isinstance(data, list):
        raise ValueError("data should be a list.")
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("data should be a list of dictionaries.")
    if not isinstance(key, str):
        raise ValueError("key should be a string.")
    if not isinstance(threshold, int):
        raise ValueError("threshold should be an int.")

    result = []
    for item in data:
        if key not in item:
            raise KeyError(f"Key {key} not found in dictionary.")
        if not isinstance(item[key], (str, int)):
            raise ValueError("Values of dictionary should be strings or int.")
        if isinstance(item[key], int) and item[key] > threshold:
            result.append(item)
        elif isinstance(item[key], str) and int(item[key]) > threshold:
            result.append(item)
    return result

def aggregate_data(
    data: List[Dict[str, Union[int, str]]], key: str
) -> Dict[str, int]:
    """Aggregate data by a given key and count occurrences.

    Args:
        data: The list of data to aggregate.
        key: The key to aggregate by.

    Returns:
        A dictionary with the aggregated data.

    Raises:
        ValueError: if data is not a list of dictionaries.
        ValueError: if key is not a string.
        KeyError: if key is not found in a dictionary.
    """
    if not isinstance(data, list):
        raise ValueError("data should be a list.")
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("data should be a list of dictionaries.")
    if not isinstance(key, str):
        raise ValueError("key should be a string.")

    result = {}
    for item in data:
        if key not in item:
            raise KeyError(f"Key {key} not found in dictionary.")
        if not isinstance(item[key], (str, int)):
            raise ValueError("Values of dictionary should be strings or int.")
        val = str(item[key])
        result[val] = result.get(val, 0) + 1

    return result
