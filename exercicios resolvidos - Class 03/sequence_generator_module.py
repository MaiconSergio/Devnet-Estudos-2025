class SequenceGenerator:
    """
    A class containing a method to generate a sequence of integers.
    """

    @staticmethod
    def generate_sequence(n):
        """
        Generates a sequence of integers from 1 to n.
        """
        return list(range(1, n + 1))