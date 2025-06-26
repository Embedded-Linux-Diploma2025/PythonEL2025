"""Write a Python program to count the number 4 in a given list."""

list = [1,4,6,7,4]


def count(lst):
    """Write your solution here. Don't forget to return the result at the end."""
    count_of_num = 0

    for i in lst:
        
        if i == 4:

            count_of_num = count_of_num +1

        else:

            """ do nothing """

    print(count_of_num)
    return count_of_num

if __name__ == "__main__":
    assert count([1, 2, 3, 4, 5, 4, 6]) == 2, "Test case failed"
    assert count([1, 2, 3, 5, 6]) == 0, "Test case failed"
    assert count([4, 4, 4, 4]) == 4, "Test case failed"
    assert count([]) == 0, "Test case failed"
    assert count([4, 5, 6, 7, 8]) == 1, "Test case failed"
    assert count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1, "Test case failed"
