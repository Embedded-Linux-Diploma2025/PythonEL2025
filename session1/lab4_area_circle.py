"""Write a Python program which accepts the radius of a circle and compute the area."""
import math

def area(number1):
    """Area of Circle is pi * r**2"""
    # """
    # Write a Python program which accepts the radius of a circle from the argument
    # and compute the area. Don't forget to return the result at the end.
    # """
    a:float = number1*number1 * math.pi
    return a
print(area(2))
print(area(1))
print(area(0))
print(area(5))

if __name__ == "__main__":
    assert area(2) == 12.566370614359172, "Test case failed"
    assert area(1) == 3.141592653589793, "Test case failed"
    assert area(0) == 0.0, "Test case failed"
    assert area(5) == 78.53981633974483, "Test case failed"
