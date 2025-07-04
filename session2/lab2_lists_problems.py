"""List Problems - Testing student capability with list operations."""
from functools import reduce

def find_max_min(numbers):
    """Find the maximum and minimum values in a list of numbers.

    Args:
        numbers (list): List of numbers

    Returns:
        tuple: (max_value, min_value)
    """
    # Write your solution here
    l=len(numbers)
    max_value=numbers[0]
    min_value=numbers[0]
    for i in range(l):
        if numbers[i]>max_value:
            max_value=numbers[i]
        if numbers[i]<min_value:
            min_value=numbers[i]
    return (max_value,min_value)


def reverse_list(items):
    """Reverse a list without using built-in reverse() method.

    Args:
        items (list): List to reverse

    Returns:
        list: Reversed list
    """
    # Write your solution here
    i = 0
    j = len(items) - 1
    k = len(items) // 2
    for i in range(k):
        swap = items[j - i]
        items[j - i] = items[i]
        items[i] = swap
    return items


def list_statistics(numbers):
    """Calculate basic statistics for a list of numbers.

    Args:
        numbers (list): List of numbers

    Returns:
        dict: Dictionary with sum, average, count
    """
    # Write your solution here
    summ=0
    count = len(numbers)
    for i in numbers:
        summ+=i
    average=summ/len(numbers)
    return {"sum" : summ, "average" : average , "count" : count}

def flatten_nested_list(nested_list):
    """Flatten a nested list structure.

    Args:
        nested_list (list): List containing sublists

    Returns:
        list: Flattened list
    """
    # Write your solution here

    return list(reduce(lambda x, y: x + y, nested_list, []))




if __name__ == "__main__":
    # Test cases
    print("Testing find_max_min...")
    result = find_max_min([1, 5, 3, 9, 2])
    assert result == (9, 1), f"Expected (9, 1), got {result}"

    print("Testing reverse_list...")
    result = reverse_list([1, 2, 3, 4, 5])
    assert result == [5, 4, 3, 2, 1], f"Expected [5, 4, 3, 2, 1], got {result}"

    print("Testing list_statistics...")
    result = list_statistics([1, 2, 3, 4, 5])
    expected = {"sum": 15, "average": 3.0, "count": 5}
    assert result == expected, f"Expected {expected}, got {result}"

    print("Testing flatten_nested_list...")
    result = flatten_nested_list([[1, 2], [3, 4], [5, 6]])
    assert result == [1, 2, 3, 4, 5, 6], f"Expected [1, 2, 3, 4, 5, 6], got {result}"

    print("All tests passed!")
