"""Write a Python program which accepts the radius of a circle and compute the area."""

"""Write a Python program which accepts the radius of a circle and compute the area."""
#import sys
import math


def area(radius):
    """
    Write a Python program which accepts the radius of a circle from the argument
    and compute the area. Don't forget to return the result at the end.
    """
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a numeric value.")
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    c_area = math.pi * (radius ** 2)
    return c_area 

if __name__ == "__main__":
    assert area(2) == 12.566370614359172, "Test case failed"
    assert area(1) == 3.141592653589793, "Test case failed"
    assert area(0) == 0.0, "Test case failed"
    assert area(5) == 78.53981633974483, "Test case failed"
