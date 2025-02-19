# Lab: Clean Code Basics

## Introduction

This lab offers an opportunity to observe basic clean code practices. Pay attention to code readability, organization, and documentation, which are essential aspects of writing maintainable and understandable code.

In this lab, you will explore the basics of Python by creating a list of numbers and computing their squares using both a for loop and a list comprehension. These are fundamental concepts that you will use often in Python programming.

## Steps

### 1. Initial Code

#### Using List Comprehension
```python
a = [1, 2, 3, 4, 5]
b = [c ** 2 for c in a]
print(b)
```

#### Using a `for` Loop
```python
a = [1, 2, 3, 4, 5]
b = []
for c in a:
    b.append(c ** 2)
print(b)
```

### 2. Variables Names

- Use descriptive and meaningful names.
- Keep it short but not too short.
- Be consistent in naming conventions across the entire project.
- Maintain consistency in naming conventions throughout your code.
- Avoid using single letters.
- Avoid using special characters or spaces.
- Avoid using keywords.

#### Using List Comprehension
```python
numbers = [1, 2, 3, 4, 5]
squares = [each_num ** 2 for each_num in numbers]
print(squares)
```

#### Using a `for` Loop
```python
numbers = [1, 2, 3, 4, 5]
squares = []
for each_num in numbers:
    squares.append(each_num ** 2)
print(squares)
```

### 3. Comments in Code

- Write comments that are brief yet describe the purpose or functionality of a code segment. Avoid unnecessary comments.
- Keep comments updated as code evolves to avoid misinformation.
- Use comments to explain complex or non-intuitive code, not obvious code.
- Keep inline comments to a minimum; they should not clutter the code.
- Use `TODO` to note incomplete tasks and `FIXME` for marking bugs or issues.

Maintaining meaningful and updated comments enhances code readability and maintainability.

#### Using List Comprehension
```python
# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use a list comprehension to compute the squares
squares = [num ** 2 for num in numbers]

# Print the resulting 'squares' list
print(squares)  # Expected Output: [1, 4, 9, 16, 25]
```

#### Using a `for` Loop
```python
# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Initialize an empty list to store the squares
squares = []

# Use a for loop to compute the squares and append them to the 'squares' list
for num in numbers:
    squares.append(num ** 2)

# Print the resulting 'squares' list
print(squares)  # Expected Output: [1, 4, 9, 16, 25]
```

### 3. Docstrings 

- **Definition:** Docstrings are in-code documentation in Python used for describing the purpose and usage of functions, classes, modules, and methods.
- **Usage:** They are written between triple double quotes and are located immediately after the function, class, or method definition.
- **Benefits:** They support readability, maintainability, and are accessible via the `help()` function, enhancing developer collaboration.

#### Using List Comprehension
```python
"""
This script creates a list of numbers and computes their squares using a list comprehension.
"""

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use a list comprehension to compute the squares
squares = [num ** 2 for num in numbers]

# Print the resulting 'squares' list
print(squares)  # Expected Output: [1, 4, 9, 16, 25]
```

#### Using a `for` Loop
```python
"""
This script creates a list of numbers and computes their squares using a for loop.
"""

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Initialize an empty list to store the squares
squares = []

# Use a for loop to compute the squares and append them to the 'squares' list
for num in numbers:
    squares.append(num ** 2)

# Print the resulting 'squares' list
print(squares)  # Expected Output: [1, 4, 9, 16, 25]
```

## Conclusion
Congratulations! You have successfully completed the lab. You have had a chance to observe and practice clean code principles, contributing to better code quality and maintainability.

Additionally, you have learned how to create lists of numbers, compute their squares using both a `for` loop and a list comprehension, and document your code using docstrings in Python. These skills will be foundational as you continue to explore Python programming.