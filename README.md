# The Socratic Debugger: An AI Prompt for Guided Learning 🧠

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Prompt Version](https://img.shields.io/badge/Prompt-1.0-brightgreen.svg)](AI_Debugging_Prompt.md)

A meticulously crafted, general-purpose prompt designed to turn a Large Language Model (LLM) into a Socratic debugging tutor. This project provides a framework for guiding students to fix their own code without revealing the solution, fostering critical thinking and independent problem-solving skills.

## ✨ Key Features

* **Pedagogical Focus**: Prioritizes learning over answer-giving.
* **Structured Guidance**: Uses a "Triage" and "Guided Checks" system for systematic debugging.
* **Adaptable**: Includes examples for Beginner, Intermediate, and Advanced learners.
* **Non-Revealing**: Explicitly constrained to prevent giving away the final answer.
* **Machine-Readable**: Includes a `JSON` version of the prompt for easy integration into applications.

---

## 🚀 Demonstration: The Prompt in Action

Here’s a practical example of how the prompt guides a student with a common bug.

| Buggy Python Code (`intermediate/example1_buggy.py`)                                                                                                                                              | Structured AI Hints (`intermediate/example1_ai_hints.md`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ```python # Problem: Check for duplicate values. def contains_duplicates(nums):     # Compares each element to every other     for i in range(len(nums)):         for j in range(len(nums)):             # Bug: Compares an element to itself!             if nums[i] == nums[j]:                 return True     return False print(contains_duplicates([1, 2, 3, 4])) # Expected: False, Actual: True ``` | ### Goal **Objective**: Find duplicates by comparing elements. **Concepts**: Nested loops, list indexing, conditional logic. <br/><hr/> ### Triage * Possible Bug: The comparison logic is flawed. * Possible Bug: The function returns too early. <br/><hr/> ### Guided Checks 1.  **Trace the Indices**: Add `print(f"Comparing index i={i} with j={j}")`. 2.  **Inspect the Values**: Also print the values `nums[i]` and `nums[j]`. 3.  **Analyze the First Step**: Run the code. A duplicate means the same value at **different indices**. Is your code checking if the indices are different? |

---

## 📂 Repository Structure

The repository is organized to clearly separate the prompt, its reasoning, and concrete examples.
