import pytest
from listcalculator_module import ListCalculator

def test_square_numbers():
    """
    Test the square_numbers method of the Calculator class.
    """
    number_list = [7, 8, 9]
    expected_output = [49, 64, 81]
    assert ListCalculator.square(number_list) == expected_output

test_square_numbers()