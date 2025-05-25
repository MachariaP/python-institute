# Python Essentials 1 - Module 3: Control Structures and Lists

*Created: May 24, 2025*

---

## Overview
Module 3 introduces control structures and list processing, enabling you to control program flow and manage collections of data. You’ll learn how to make decisions, repeat tasks, and work with lists, along with logical and bitwise operations.

## Objectives
- Use Boolean values and conditional statements.
- Implement loops for repetitive tasks.
- Process lists and perform logical/bitwise operations.

## Topics Covered
- **Boolean Values**: `True`, `False`, and logical operators (`and`, `or`, `not`).
- **Conditional Execution**:
  - `if`, `elif`, `else` statements.
  - Nested conditionals.
- **Loops**:
  - `for` loops for iterating over sequences.
  - `while` loops for condition-based repetition.
- **Lists**:
  - Creating and manipulating lists (e.g., `my_list = [1, 2, 3]`).
  - List methods: `append()`, `remove()`, `sort()`, etc.
  - List slicing and indexing.
- **Logical and Bitwise Operations**:
  - Logical: `and`, `or`, `not`.
  - Bitwise: `&`, `|`, `^`, `~`, `<<`, `>>`.

## Getting Started
1. **Set Up**: Ensure Python and your editor are ready.
2. **Try It**:
   - Create a file: `nano loops.py`.
   - Example code:
     ```python
     numbers = [1, 2, 3, 4, 5]
     for num in numbers:
         if num % 2 == 0:
             print(f"{num} is even")
     ```
   - Run: `python loops.py`.
3. **Explore**: Check the `module3/` folder for example code and exercises.

## Why This Matters
Control structures and lists allow you to build dynamic programs that make decisions and handle multiple data items. These skills are critical for tasks like data processing and automation.

## Next Steps
- Complete the exercises in the `module3/` folder.
- Proceed to [Module 4](../module4/README.md) to learn about functions and advanced data structures.
