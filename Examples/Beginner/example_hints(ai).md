# AI Debugging Hints: Beginner Example 

### Goal

* **Objective**: Correctly sum all numbers in a list using a loop.
* **Concepts**: Observe how a `for` loop iterates and how a variable can be used to accumulate a value over multiple iterations.

### Triage

This section lists potential areas where bugs might occur in this type of problem. Check if your code might have one of these issues.

* **Possible Bug**: The loop might not be iterating through all the numbers in the list.
* **Possible Bug**: The variable holding the sum (`total`) is being reset or assigned an incorrect value inside the loop.
* **Possible Bug**: The final `return` statement is misplaced (e.g., inside the loop).

### Guided Checks

Follow these steps to diagnose the issue in your code.

1.  **Verify the Loop**: Add `print(number)` as the first line inside your `for` loop. Run the code. Does it print every single number from the input list?
2.  **Inspect the Accumulator**: After your `print(number)` line, add `print(f"Total is now: {total}")`. Run the code again. Watch how the value of `total` changes with each iteration. Is it growing as you would expect a sum to grow?
3.  **Review the Operation**: Look at the line `total = number`. This is an **assignment** operation. To create a sum, you need an **accumulation** operation. Think about how you would *add* the `number` to the existing `total` rather than replacing it.