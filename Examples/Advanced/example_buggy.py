# Problem: Implement binary search on a sorted array.

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    # Bug: Fails when target is the last element to be checked (e.g., at arr[0] or arr[high])
    while low < high: 
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Test cases
sorted_list = [2, 5, 7, 8, 11, 12]
print(f"Searching for 12: {binary_search(sorted_list, 12)}")
# Expected output: 5
# Actual output: -1