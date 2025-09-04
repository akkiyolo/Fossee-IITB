# The Socratic Debugger: An AI Prompt for Guided Learning 🧠

<img width="600" height="230" alt="image" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1ZKNTsSs6ujH6-0NfrCe1hgBq3WGZbE32lA&s" />

</br>

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

| Buggy Python Code (`intermediate/example_buggy.py`)                                                                                                                                              | Structured AI Hints (`intermediate/example_hints(ai).md`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ```python # Problem: Check for duplicate values. def contains_duplicates(nums):     # Compares each element to every other     for i in range(len(nums)):         for j in range(len(nums)):             # Bug: Compares an element to itself!             if nums[i] == nums[j]:                 return True     return False print(contains_duplicates([1, 2, 3, 4])) # Expected: False, Actual: True ``` | ### Goal **Objective**: Find duplicates by comparing elements. **Concepts**: Nested loops, list indexing, conditional logic. <br/><hr/> ### Triage * Possible Bug: The comparison logic is flawed. * Possible Bug: The function returns too early. <br/><hr/> ### Guided Checks 1.  **Trace the Indices**: Add `print(f"Comparing index i={i} with j={j}")`. 2.  **Inspect the Values**: Also print the values `nums[i]` and `nums[j]`. 3.  **Analyze the First Step**: Run the code. A duplicate means the same value at **different indices**. Is your code checking if the indices are different? |

---

## 📂 Repository Structure

The repository is organized to clearly separate the prompt, its reasoning, and concrete examples.

```text
FOSSEE-IITB/
│
├── AI_Debugging_Prompt(Natural Language).md       # Human-readable AI prompt
├── AI_Debugging_Prompt.json     # Machine-readable AI prompt
├── examples/                    # Skill-level examples demonstrating AI guidance
│   ├── Beginner/
│   │   ├── example_buggy.py
│   │   ├── example1_hints(ai).md
│   ├── intermediate/
│   │   ├── example1_buggy.py
│   │   └── example1_hints(ai).md
│   └── advanced/
│       ├── example1_buggy.py
│       └── example1_hints(ai).md
├── Socratic_AI(Research).pdf  # 15-page detailed rationale
└── LICENSE                      # MIT License

```

---

## 🤖 The Core Prompt

This is the central instruction set provided to the AI. It establishes the persona, rules, and structured output format.

<details>
<summary><strong>Click to expand and view the full AI Prompt</strong></summary>

```markdown
You are a Socratic Python Debugging Assistant. Your primary role is to act as a friendly and encouraging programming tutor for a student. You must help them identify and fix bugs in their Python code on their own.

Your goal is NOT to give the student the correct answer or the fixed code. Your purpose is to guide them to discover the solution themselves, thereby improving their debugging and problem-solving skills.

When a student submits their buggy Python code and the problem description, follow these steps precisely:

1.  **Acknowledge and Encourage:** Start with a positive and encouraging tone. Acknowledge the effort they've put in.

2.  **Analyze and Understand:** Carefully analyze the student's code in relation to the problem description they provide. Identify the logical errors, syntax errors, or edge cases they might have missed.

3.  **Guide, Don't Tell (The Core Rule):**
    * **DO NOT** provide the corrected code snippet.
    * **DO NOT** write the line of code that fixes the bug.
    * **DO NOT** explicitly state "The error is X, and it's because you did Y."

4.  **Provide Structured Hints:** Instead of giving the solution, generate a response in a clear markdown format with three sections: "Goal," "Triage," and "Guided Checks."
    * **Goal**: Briefly state the objective of the code and the key programming concepts involved.
    * **Triage**: List 2-3 *potential* high-level categories of bugs that are common for this type of problem, without confirming which one is present.
    * **Guided Checks**: Provide a numbered list of concrete, actionable steps the student can take (e.g., adding `print` statements, testing specific inputs) to find the bug themselves. These checks should lead the student to the "aha!" moment.
```
</details>

## 💡 Design Philosophy
The prompt was engineered around a few core principles:

Active Learning: The student is not a passive recipient of information. The "Guided Checks" require them to actively engage with and investigate their own code.

Systematic Problem-Solving: The "Triage" section teaches a professional debugging skill: forming hypotheses before diving in. This moves students from random guessing to a structured approach.

Clarity and Consistency: The structured output (Goal, Triage, Checks) ensures the AI's response is always predictable, easy to follow, and useful, regardless of the specific coding problem.

Psychological Safety: The process begins with encouragement, framing debugging as a normal and learnable part of programming, not a failure.

## 🛠️ Setup and Usage
* This project is a framework, not a standalone application. To use it, you will need access to a Large Language Model (LLM) that allows for detailed initial instructions (e.g., ChatGPT, Gemini, Claude).

* Initialize the Tutor: Copy the full text from AI_Debugging_Prompt(Natural Language).md and paste it as the first message to your chosen LLM. This action sets the AI's persona, its rules, and its Socratic methodology.

* Submit Your Code: In a new message, provide the buggy Python code you want to debug. Also, briefly explain the code's intended purpose and the error you are observing.


* Engage in the Dialogue: The AI will not provide a direct fix. Instead, it will respond with a structured set of hints to guide you. Follow its "Guided Checks" and report your findings to continue the dialogue. The goal is for you to discover and implement the solution yourself.

## ⚖️ Reasoning Behind the Framework
The design of this framework is grounded in established pedagogical research to create an effective and safe learning environment.

* Fostering Independent Problem-Solving: Standard LLMs often provide immediate solutions, which can hinder the development of a student's critical thinking skills. This framework intentionally constrains the AI to act as a Socratic guide, creating a "learning distance" between the problem and its solution where productive struggle and discovery can occur.

* Addressing Psychological Hurdles: Debugging can cause significant frustration and a sense of personal failure in novice programmers. The prompt engineers a patient and encouraging AI persona to mitigate these negative emotions and foster a positive "error culture" where mistakes are viewed as valuable learning opportunities.

* Structured Scaffolding: To manage the high cognitive load associated with debugging , the framework's logic is based on the research-backed 

* PRIMMDebug protocol. This structured process (Predict, Run, Spot the Defect, Inspect, Find, Fix, Test) breaks the complex task into manageable steps, preventing cognitive overload and building effective habits.

* Advanced and Safe Implementation: The prompt uses advanced engineering techniques to ensure pedagogical integrity.

## 📄 Report Highlights
This project is based on the detailed framework presented in the research paper, 

"A Pedagogically-Informed Prompting Framework for a Socratic AI Debugging Assistant". Key highlights from the report include:

* The Pedagogical Problem: The report identifies that standard LLMs undermine learning by providing direct solutions. It also addresses the significant cognitive and emotional hurdles novices face when debugging, such as frustration and a sense of failure.

* The Socratic Solution: To counter this, the framework proposes transforming an LLM into a Socratic tutor that guides students to their own conclusions. The goal is to create a "learning distance" between the problem and the solution, where productive struggle can occur.

* Research-Grounded Framework: The assistant's logic is built upon the PRIMMDebug framework (Predict, Run, Spot the Defect, Inspect, Find, Fix, Test), a research-backed method for structuring debugging that reduces cognitive load.

* Advanced Prompt Engineering: The prompt uses a combination of techniques, including Role Prompting to create a patient tutor persona , internal Chain-of-Thought (CoT) for analyzing student code without revealing the analysis , and an Adaptability Framework to adjust its questioning for novice versus advanced learners.

* Turning Weakness into Strength: The report argues that because LLMs can be "confidently inaccurate," their best use is not as an oracle but as a Socratic partner. This encourages students to become the final arbiters of correctness, teaching them the critical meta-skill of code validation.

## 🗺️ Future Directions
The framework proposed in the report serves as a robust foundation. Future work could include:


* Empirical Studies: Conducting controlled experiments in classrooms to quantitatively measure learning outcomes against other AI tools or traditional methods.


* IDE Integration: Building a plugin for IDEs like VS Code to provide real-time, context-aware Socratic guidance directly in the student's workflow.


* Multi-modal Inputs: Expanding the assistant to accept screenshots of errors or spoken-word problem descriptions to make the tool more accessible.
