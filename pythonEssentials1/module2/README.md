```markdown
# Python Essentials 1 - Module 2: The print() Function

*Created: May 26, 2025*

---

## Overview
Module 2 introduces the `print()` function in Python, a fundamental tool for outputting text to the console. This module explores various ways to use `print()`, including customizing its behavior with keyword arguments and escape characters. You’ll write and run scripts to understand how Python handles output formatting.

## Objectives
- Learn the basic usage of the `print()` function.
- Understand how to use multiple arguments and control their output.
- Explore newline and escape characters for string formatting.
- Customize `print()` behavior using `sep` and `end` keyword arguments.
- Apply best practices for writing and documenting Python scripts.

## Topics Covered
- **Basic print() Usage**:
  - Outputs text to the console, with each call starting a new line.
  - Example: `print("The itsy bitsy spider climbed up the waterspout.")`.
- **Empty print()**:
  - An empty `print()` outputs a blank line (newline, `\n`).
  - Example: `print()` adds spacing between outputs.
- **Newline and Escape Characters**:
  - `\n` creates a new line within a string.
  - `\\` outputs a single backslash.
  - Example: `print("The itsy bitsy spider\nclimbed up the waterspout.")`.
- **Multiple Arguments**:
  - `print()` accepts multiple arguments, joined by a space (default `sep=" "`).
  - Example: `print("The itsy bitsy spider", "climbed up", "the waterspout.")`.
- **Positional Arguments with end Parameter**:
  - Argument order determines output order.
  - `end` customizes the line ending (default: `\n`).
  - Example: `print("My name is", "Python.", end=" ")` followed by `print("Monty Python.")`.
- **sep Keyword Argument**:
  - `sep` customizes the separator between arguments.
  - Example: `print("My", "name", "is", "Monty", "Python.", sep="-")` outputs `My-name-is-Monty-Python.`.
- **Combining sep and end**:
  - Use both parameters to control separation and line endings.
  - Example: `print("My", "name", "is", sep="_", end="*")` followed by `print("Monty", "Python.", sep="*", end="*\n")`.

## Getting Started
1. **Navigate to the Directory**: `cd module_2/basics/`.
2. **Run Scripts**:
   - Ensure scripts are executable: `chmod +x <script_name>.py`.
   - Run: `./<script_name>.py` or `python3 <script_name>.py`.
   - Example: `./print_sep_end.py` outputs `My_name_is*Monty*Python.*`.
3. **Explore Scripts**:
   - `hello_world.py`: Prints "Hello, World!".
   - `print_basic.py`: Basic `print()` with multiple lines.
   - `print_empty.py`: Empty `print()` for blank lines.
   - `print_newline.py`: Newline and escape characters.
   - `print_multiple_args.py`: Multiple arguments with default spacing.
   - `print_positional.py`: Positional arguments with `end` parameter.
   - `print_keyword_args.py`: `sep` parameter for custom separators.
   - `print_sep_end.py`: Combined `sep` and `end` parameters.
4. **Verify Output**: Use a terminal or IDLE to check script outputs.

## Why This Matters
Mastering the `print()` function is essential for debugging and displaying output in Python programs. Understanding its parameters (`sep`, `end`) and escape characters allows you to format output effectively, preparing you for more complex programming tasks.

## Next Steps
- Proceed to explore data types, variables, or other Python fundamentals.
```
