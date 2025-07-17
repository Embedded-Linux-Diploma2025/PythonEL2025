"""Sum 1 … n — Compute and display the running total."""


def compute(number):
    # """write your soulution Here Sum 1 … n — Compute and display the running total."""
    """Sum_accumulator is the Accumulate factor"""
    sum_accumulator = 0 # initialzation for sum that will accumulate the number
    for i in range(number) :
        sum_accumulator += (i+1) #adding the current number to the Accumulator
    return sum_accumulator

print(compute(5))
print(compute(10))
print(compute(100))
print(compute(0))
print(compute(1))
print(compute(2))
print(compute(3))
print(compute(4))

if __name__ == "__main__":
    assert compute(5) == 15, "Test case failed"
    assert compute(10) == 55, "Test case failed"
    assert compute(100) == 5050, "Test case failed"
    assert compute(0) == 0, "Test case failed"
    assert compute(1) == 1, "Test case failed"
    assert compute(2) == 3, "Test case failed"
    assert compute(3) == 6, "Test case failed"
    assert compute(4) == 10, "Test case failed"
