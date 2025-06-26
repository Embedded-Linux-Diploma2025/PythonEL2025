"""Write a Python program which accepts the radius of a circle and compute the area."""
import math
def area(radius):
    """fuction accepts the radius of a circle from the argument and compute the area"""
    area_function=(math.pi)*(radius**2)
    return area_function
if __name__ == "__main__":
    assert area(2) == 12.566370614359172, "Test case failed"
    assert area(1) == 3.141592653589793, "Test case failed"
    assert area(0) == 0.0, "Test case failed"
    assert area(5) == 78.53981633974483, "Test case failed"
