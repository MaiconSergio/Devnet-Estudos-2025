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