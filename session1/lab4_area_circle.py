"""Write a Python program which accepts the radius of a circle and compute the area."""
import math

def area(number1):
    """
    Write a Python program which accepts the radius of a circle from the argument
    and compute the area. Don't forget to return the result at the end.
    """
    number1 = int(input("please enter radius of a circle: "))
    area_circle = math.pi * (number1**2)
    print(f"area is: {area_circle}")
    return area_circle

if __name__ == "__main__":
    assert area(2) == 12.566370614359172, "Test case failed"
    assert area(1) == 3.141592653589793, "Test case failed"
    assert area(0) == 0.0, "Test case failed"
    assert area(5) == 78.53981633974483, "Test case failed"
