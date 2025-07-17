"""Write a Python program to count the number 4 in a given list."""

def count_fours(lst):
    """Count the number of times 4 appears in the given list."""
    return lst.count(4)

if __name__ == "__main__":
    assert count_fours([1, 2, 3, 4, 5, 4, 6]) == 2
    assert count_fours([1, 2, 3, 5, 6]) == 0
    assert count_fours([4, 4, 4, 4]) == 4
    assert count_fours([]) == 0
    assert count_fours([4, 5, 6, 7, 8]) == 1
    assert count_fours([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
