import numpy as np

numbers = np.array([1, 6, 3, 8, 2, 7])  # Define the "numbers" array
mask = numbers > 5  # Create a boolean mask for numbers greater than 5
print("Numbers greater than 5:", numbers[mask]) 