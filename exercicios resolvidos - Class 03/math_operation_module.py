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