# Python Essentials 1 - Module 4: Functions, Data Structures, and Exceptions

*Created: May 24, 2025*

---

## Overview
Module 4 focuses on creating reusable code, working with advanced data structures, and handling errors. You’ll learn to write functions, use tuples and dictionaries, process data, and manage exceptions to build robust Python programs.

## Objectives
- Create and use functions for modular code.
- Work with tuples, dictionaries, and data processing techniques.
- Handle errors using exception handling.

## Topics Covered
- **Functions**:
  - Defining functions with `def`.
  - Parameters, return values, and scope.
  - Lambda functions and recursion.
- **Tuples**:
  - Immutable sequences (e.g., `my_tuple = (1, 2, 3)`).
  - Tuple unpacking and use cases.
- **Dictionaries**:
  - Key-value pairs (e.g., `my_dict = {"name": "Alice", "age": 25}`).
  - Dictionary methods: `get()`, `keys()`, `values()`, etc.
- **Exceptions**:
  - Handling errors with `try`, `except`, `finally`.
  - Raising exceptions with `raise`.
- **Data Processing**:
  - Reading/writing files.
  - Processing data with loops and comprehensions.

## Getting Started
1. **Set Up**: Ensure Python and your editor are ready.
2. **Try It**:
   - Create a file: `nano functions.py`.
   - Example code:
     ```python
     def greet(name):
         return f"Hello, {name}!"
     try:
         name = input("Enter your name: ")
         print(greet(name))
     except ValueError:
         print("Invalid input!")
     ```
   - Run: `python functions.py`.
3. **Explore**: Check the `module4/` folder for example code and exercises.

## Why This Matters
Functions, advanced data structures, and exception handling enable you to write modular, efficient, and error-resistant programs. These skills are essential for real-world applications like web development and data analysis.

## Next Steps
- Complete the exercises in the `module4/` folder.
- Explore advanced Python topics or frameworks like Django to build on your skills.
