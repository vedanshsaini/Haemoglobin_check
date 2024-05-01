import random
from typing import List, Union

class RandomNumberGenerator:
    """
    A class to generate random numbers based on given probabilities.

    Attributes:
        numbers (List[int]): A list of integers representing the possible random numbers.
        probabilities (List[float]): A list of floats representing the probability of each corresponding number in `numbers`.
        cumulative_probabilities (List[float]): A list of cumulative probabilities calculated from `probabilities`.
    """

    def __init__(self, numbers: List[int], probabilities: List[float]):
        """
        Initialize the RandomNumberGenerator with the given numbers and probabilities.

        Args:
            numbers (List[int]): A list of integers representing the possible random numbers.
            probabilities (List[float]): A list of floats representing the probability of each corresponding number in `numbers`.

        Raises:
            ValueError: If the lengths of `numbers` and `probabilities` are not equal, or if the sum of probabilities is not 1.0.
        """
        if len(numbers) != len(probabilities):
            raise ValueError("The length of the numbers list must be equal to the length of the probabilities list.")

        if not isclose(sum(probabilities), 1.0):
            raise ValueError("The sum of probabilities must be equal to 1.0.")

        self.numbers = numbers
        self.probabilities = probabilities
        self.cumulative_probabilities = [sum(probabilities[:i + 1]) for i in range(len(probabilities))]

    def nextNum(self) -> Union[int, None]:
        """
        Generate a random number based on the given probabilities.

        Returns:
            int or None: A random number from the `numbers` list, selected based on the given probabilities.
                         If an error occurs, returns None.
        """
        try:
            random_value = random.random()
            for i, cumulative_probability in enumerate(self.cumulative_probabilities):
                if random_value < cumulative_probability:
                    return self.numbers[i]
            # This line should never be reached, but it's included for completeness
            return self.numbers[-1]
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

def isclose(a: float, b: float, rel_tol: float = 1e-09, abs_tol: float = 0.0) -> bool:
    """
    Helper function to compare floats for equality with a tolerance.

    Args:
        a (float): The first float value.
        b (float): The second float value.
        rel_tol (float): The relative tolerance for the comparison.
        abs_tol (float): The absolute tolerance for the comparison.

    Returns:
        bool: True if the two floats are considered equal within the specified tolerances, False otherwise.
    """
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def main():
    """
    Example usage of the RandomNumberGenerator class.
    """
    numbers = [-1, 0, 1, 2, 3]
    probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]

    generator = RandomNumberGenerator(numbers, probabilities)

    # Generate 100 random numbers
    results = [generator.nextNum() for _ in range(100)]

    # Count the occurrences of each number
    count = {num: results.count(num) for num in numbers}
    print(count)

if __name__ == "__main__":
    main()