# AI Debugging Hints: Advanced Example 1

### Goal

* **Objective**: Correctly implement a binary search algorithm to find a target in a sorted array.
* **Concepts**: Loop termination conditions (`while`), integer division for calculating the midpoint, and pointer manipulation (`low`, `high`).

### Triage

This section lists potential areas where bugs might occur in this type of problem. These are classic pitfalls in search algorithms.

* **Possible Bug**: The `mid` point is being calculated incorrectly, potentially leading to an infinite loop or skipping elements.
* **Possible Bug**: The `low` and `high` pointers are not being updated correctly after a comparison (e.g., `high = mid` instead of `high = mid - 1`).
* **Possible Bug**: The `while` loop's condition is causing it to stop one iteration too early or one too late (an "off-by-one" error).

### Guided Checks

Follow these steps to diagnose the issue in your code.

1.  **Trace the Pointers**: Add `print(f"low: {low}, high: {high}, mid: {mid}")` as the first line inside your `while` loop.
2.  **Test the Boundaries**: Run your code with a target that you know fails, specifically the **very first** or **very last** element in the list (e.g., `2` or `12` in the example). Watch the trace output.
3.  **Examine the Final State**: Look at the last line of your printed output before the loop ends. What are the values of `low` and `high`? Now, look at your `while` loop's condition (`while low < high`). When `low` and `high` are equal, should the loop run one final time to check that last possible element? Does your current condition allow for that?