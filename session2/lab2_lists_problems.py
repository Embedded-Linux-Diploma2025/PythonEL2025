"""List Problems - Testing student capability with list operations."""
def find_max_min(numbers):
    """max and min of list"""
    return max(numbers),min(numbers)
def reverse_list(items):
    """reverse of list"""
    return items[::-1]
def list_statistics(numbers):
    """sum avg count of list"""
    if len(numbers)==0:
        return{
            "sum": 0,
            "average": 0,
            "count": 0
        }
    list_count=len(numbers)
    total=sum(numbers)
    avg=total/list_count
    return{
        "sum": total,
        "average": avg,
        "count": list_count
    }
def flatten_nested_list(nested_list):
    """flattens nested list"""
    flatten_lst=[]
    for sublist in nested_list:
        for num in sublist:
            flatten_lst.append(num)
    return flatten_lst
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
