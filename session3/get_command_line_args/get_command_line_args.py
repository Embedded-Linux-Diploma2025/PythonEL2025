"""Get argumebts from command line. user must enter 4 arguments (file name and three numbers)"""
import sys

def add(num1, num2, num3):
    """Add the numbers."""
    return int(num1) + int(num2) + int(num3)

if __name__ == "__main__":
    sum_of_numbers = add(sys.argv[1], sys.argv[2], sys.argv[3])
    print(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3])
    print(sum_of_numbers)
