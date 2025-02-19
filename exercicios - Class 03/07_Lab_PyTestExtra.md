# Lab: Testing Exceptions with PyTest

### Objective

Expand our current modules to handle potential mathematical exceptions. In this lab, we will modify the `MathOperations` module to handle division by zero and test if the exceptions are raised correctly.

### Prerequisites: Completion of the previous unit testing and integration testing labs.

### 1. Modify the MathOperations Module
Let's consider the scenario where division by zero might occur in our `MathOperations` module. This should result in an exception. Adjust the `MathOperations` module to manage this:

**math_operations_module.py**:
```python
class MathOperations:
    """
    A class containing basic mathematical operations.
    """
    
    @staticmethod
    def divide(numerator, denominator):
        """
        Divides numerator by denominator.
        """
        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return numerator / denominator
```

### 2. Create Exception Test
Now, add a test in our existing test module, `test_math_operations.py`. This test will ensure that the `divide` method raises an exception when attempting to divide by zero:

**test_math_operations.py**:
```python
import pytest
from math_operations_module import MathOperations

def test_divide_by_zero_exception():
    """
    Test if the divide method raises an exception when dividing by zero.
    """
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero!"):
        MathOperations.divide(10, 0)
```

### 3. Run Exception Test
Navigate to the project directory in your terminal and run the exception test using the following command:

```bash
pytest test_math_operations.py -k test_divide_by_zero_exception
```

Observe the results. If the exception test is successful, PyTest will display a message indicating successful execution. If the test fails, PyTest will provide detailed information about the discrepancy.

## Conclusion
This lab illustrated how to write tests that verify whether exceptions are raised as anticipated in our modules. Exception testing ensures that our software behaves as expected under unanticipated circumstances, improving its resilience and dependability.

---

I hope this version aligns well with the desired style and format!