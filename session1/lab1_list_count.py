"""Write a Python program to count the number 4 in a given list."""
def count(lst):
    """return number of number (4) in list"""
    ctr=0 # counter for number "4"
    for i in lst:
        if i== 4:
            ctr+=1
    return ctr # return counter value
if __name__ == "__main__":
    assert count([1, 2, 3, 4, 5, 4, 6]) == 2, "Test case failed"
    assert count([1, 2, 3, 5, 6]) == 0, "Test case failed"
    assert count([4, 4, 4, 4]) == 4, "Test case failed"
    assert count([]) == 0, "Test case failed"
    assert count([4, 5, 6, 7, 8]) == 1, "Test case failed"
    assert count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1, "Test case failed"
