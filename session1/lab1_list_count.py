"""Write a Python program to count the number 4 in a given list."""



def count(lst):
    """Write your solution here. Don't forget to return the result at the end."""
    x = 4
    counter = 0
    n = len(lst)
    for i in range(n):
        if lst[i] == x:
            counter = counter + 1
    return counter





if __name__ == "__main__":
    assert count([1, 2, 3, 4, 5, 4, 6]) == 2, "Test case failed"
    assert count([1, 2, 3, 5, 6]) == 0, "Test case failed"
    assert count([4, 4, 4, 4]) == 4, "Test case failed"
    assert count([]) == 0, "Test case failed"
    assert count([4, 5, 6, 7, 8]) == 1, "Test case failed"
    assert count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1, "Test case failed"
