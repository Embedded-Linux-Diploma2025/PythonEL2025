"""Write a Python program which accepts the radius of a circle and compute the area."""


def area(number1):
    """ area =  pi * radius squared """
    pi = 3.141592653589793
    return number1 ** 2 * pi


if __name__ == "__main__":
    assert area(2) == 12.566370614359172, "Test case failed"
    assert area(1) == 3.141592653589793, "Test case failed"
    assert area(0) == 0.0, "Test case failed"
    assert area(5) == 78.53981633974483, "Test case failed"
