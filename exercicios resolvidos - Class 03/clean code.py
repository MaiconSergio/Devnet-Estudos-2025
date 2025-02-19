from typing import List

def square(numbers: List[float]) -> List[float]:
    """
    Squares each number in the list.
    :param numbers: List of numbers to be squared.
    :return: List of squared numbers.
    """
    return [each_num ** 2 for each_num in numbers]
from typing import List, Union

def divide(numbers: List[Union[int, float]], divisor: Union[int, float]) -> List[Union[int, float]]:
    """
    Divides each number in the list by the divisor.
    :param numbers: List of dividends.
    :param divisor: The divisor.
    :return: List of results of the division.
    """
    # FIXME: Handle division by zero
    return [each_num / divisor for each_num in numbers]


list_number = [1,2,3,4,5]
divisor = 2

print("o resultado é:", square(list_number ))
print("o resultado da divisão é:", divide(list_number, divisor))