# Problem: Write a function to check if a list contains any duplicate values.

def contains_duplicates(nums):
    # Check for duplicates by comparing each element to every other element
    for i in range(len(nums)):
        for j in range(len(nums)):
            # Bug: This compares an element with itself, always returning True for non-empty lists.
            if nums[i] == nums[j]:
                return True
    return False

# Test cases
print(f"List [1, 2, 3, 4] has duplicates: {contains_duplicates([1, 2, 3, 4])}")
# Expected output: False
# Actual output: True