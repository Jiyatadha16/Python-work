#write a NumPy program to find the number of elements of an array, length of one array element in bytes and total bytes consumed by the elements.

import numpy as np

# Create a NumPy array
arr = np.array([10, 20, 30, 40, 50], dtype=np.int32)

# Number of elements
num_elements = arr.size

# Length of one element in bytes
element_size = arr.itemsize

# Total bytes consumed
total_bytes = arr.nbytes

print("Array:", arr)
print("Number of elements:", num_elements)
print("Size of one element (bytes):", element_size)
print("Total bytes consumed:", total_bytes)


