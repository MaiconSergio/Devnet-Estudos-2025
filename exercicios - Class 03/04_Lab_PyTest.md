# Lab: PyTest and Good Practices

## Introduction

In this lab, we will learn about PyTest, a testing framework for Python that allows for simple unit tests as well as complex functional testing. We'll apply the good practices we've learned earlier and structure our code in a modular way.

### Objective

- Create a module for a class containing a method to square a list of numbers.
- Write the main application that will use this module.
- Write a separate test module using PyTest to test our function.

### 1. Creating the Module

Create a file named `list_calculator_module.py`. This file will contain a class with a method to square a list of numbers. Apply the good practices we have learned for naming and documenting the code.

```python
class ListCalculator:
    """
    A class that contains methods to perform mathematical operations.
    """
    
    @staticmethod
    def square(numbers):
        """
        Squares each number in the list.
        :param numbers: List of numbers to be squared.
        :return: List of squared numbers.
        """
        return [each_num ** 2 for each_num in numbers]
```

### 2. Writing the Main Application

Create a file named `main.py`. This will be the main application file that will import and use the `list_calculator_module.py`.

```python
from list_calculator_module import ListCalculator

# Define a list of numbers
number_list = [1, 2, 3, 4, 5]

# Use the Calculator class from the calculator_module to square the list of numbers
squared_list = ListCalculator.square(number_list)

# Print the result
print("Original List:", number_list)
print("Squared List:", squared_list)
```

### 3. Writing the Test Module

Create another file named `test_list_calculator.py`. This will be our testing module. We will write a PyTest function to test the `square` method of the `ListCalculator` class.

```python
import pytest
from list_calculator_module import ListCalculator

def test_square_numbers():
    """
    Test the square_numbers method of the Calculator class.
    """
    number_list = [7, 8, 9]
    expected_output = [49, 64, 81]
    assert ListCalculator.square(number_list) == expected_output

test_square_numbers()
```

### 4. Running the Tests

Navigate to the directory containing your files in your terminal, and run the PyTest command:

```sh
pytest test_calculator.py
```

Observe the output. If everything is correct, all tests should pass.

## Conclusion

Congratulations! You have successfully created a modular application using good coding practices, written unit tests using PyTest, and ensured that your code is working as expected. This approach ensures maintainability and reliability in software development. Keep practicing these concepts to enhance your coding skills!