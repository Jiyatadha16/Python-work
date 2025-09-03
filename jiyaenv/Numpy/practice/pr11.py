#write a NumPy program to find a set difference of two arrays. The set difference will return the sorted, unique values in array1 that are not in array2.

import numpy as np

# Define two arrays
array1 = np.array([1, 2, 3, 4, 5, 6])
array2 = np.array([4, 5, 6, 7, 8, 9])

# Find the set difference
set_diff = np.setdiff1d(array1, array2)

print("Array1:", array1)
print("Array2:", array2)
print("Set difference (Array1 - Array2):", set_diff)


