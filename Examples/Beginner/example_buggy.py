# Problem: Write a function to calculate the sum of a list of numbers.

def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total = number # Bug: This overwrites the total in each loop.
    return total

# Test case
print(f"The sum of [1, 2, 3, 4, 5] is: {calculate_sum([1, 2, 3, 4, 5])}")
# Expected output: 15
# Actual output: 5