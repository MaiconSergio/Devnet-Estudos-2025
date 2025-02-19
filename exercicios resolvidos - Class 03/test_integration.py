import pytest
from sequence_generator_module import SequenceGenerator
from listcalculator_module import ListCalculator


def test_integration():
    """
    Test the integration of the generate_sequence method from SequenceGenerator 
    and square method from ListCalculator.
    """
    n = 3
    
    # Generate a sequence
    sequence = SequenceGenerator.generate_sequence(n)
    
    # Check if the output type of generate_sequence matches the input type of square
    assert isinstance(sequence, list), "The output of generate_sequence should be a list"
    assert all(isinstance(num, int) for num in sequence), "All elements in the sequence should be integers"
    
    # Calculate the square of the sequence and check if the output is as expected
    squared_list = ListCalculator.square(sequence) 
    assert squared_list == [1, 4, 9], "The squared list is not as expected"