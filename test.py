def flatten_nested_list(nested_list):
    """Flatten a nested list structure.

    Args:
        nested_list (list): List containing sublists

    Returns:
        list: Flattened list
    """
    # Write your solution here
    result = []
    for sublist in nested_list:
        for element in sublist:
            result.append(element)
    return result

a = [[1, 2], [3, 4], [5, 6]]
print(flatten_nested_list(a))