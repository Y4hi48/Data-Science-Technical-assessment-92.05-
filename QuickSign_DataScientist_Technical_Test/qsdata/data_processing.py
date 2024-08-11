"""Module containing data processing for dicts."""


def filter_data(
    data: list[dict[str, int | str]], key: str, value: int | str
) -> list[dict[str, int | str]]:
    """Filter data to keep only the items where data[key] == value.

    Args:
        data : The list of data to filter.
        key : The key to filter by.
        value: The value to match.

    Returns:
        A list of dictionaries that match the filter criteria.
    """
    # pass
    if not isinstance(data, list):
        raise ValueError("Wrong Input!! Data must be a list")

    for item in data:
        if not isinstance(item, dict):
            raise ValueError(
                "All elements in the data list must be dictionaries"
            )

    return [item for item in data if item.get(key) == value]


def sort_data(
    data: list[dict[str, int | str]], key: str
) -> list[dict[str, int | str]]:
    """Sort a list of dictionaries by a specified key.

    Args:
        data : The list of data to sort.
        key : The key to sort by.

    Returns:
        A list of dictionaries sorted by the specified key.
    """
    return sorted(data, key=lambda x: x[key])


def complex_filter(
    data: list[dict[str, int | str]], key: str, threshold: int
) -> list[dict[str, int | str]]:
    """Filter data using a threshold condition.

    Args:
        data: The list of data to filter.
        key: The key to filter by.
        threshold: The threshold value.

    Returns:
        A list of dictionaries that match the threshold criteria.
    """
    # pass
    if not isinstance(data, list):
        raise ValueError("Data must be a list")

    for item in data:
        if not isinstance(item, dict):
            raise ValueError(
                "All elements in the data list must be dictionaries"
            )
        if key not in item:
            raise ValueError(
                f"Key '{key}' not found in one or more dictionaries"
            )
        if not isinstance(item[key], int):
            raise ValueError(f"Key '{key}' must correspond to integer values")

    return [item for item in data if item[key] > threshold]


def aggregate_data(
    data: list[dict[str, int | str]], key: str
) -> dict[str, int]:
    """Aggregate data by a given key and count occurrences.

    Args:
        data: The list of data to aggregate.
        key: The key to aggregate by.

    Returns:
        A dictionary where the keys are the unique values from the specified key in the input data,
        and the values are the counts of those unique values.
    """

    aggregation = {}
    for item in data:
        value = item[key]
        if value in aggregation:
            aggregation[value] += 1
        else:
            aggregation[value] = 1

    return aggregation
