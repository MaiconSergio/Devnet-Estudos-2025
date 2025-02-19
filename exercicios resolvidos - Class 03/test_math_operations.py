import pytest
from math_operation_module import MathOperations

def test_divide_by_zero_exception():
    """
    Test if the divide method raises an exception when dividing by zero.
    """
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero!"):
        MathOperations.divide(10, 0)