#write a NumPy program to convert a list and tuple into arrays…

import numpy as np

# Python list
py_list = [1, 2, 3, 4, 5]

# Python tuple
py_tuple = (6, 7, 8, 9, 10)

# Convert list to NumPy array
arr_from_list = np.array(py_list)

# Convert tuple to NumPy array
arr_from_tuple = np.array(py_tuple)

print("Original List:", py_list)
print("NumPy Array from List:", arr_from_list)

print("\nOriginal Tuple:", py_tuple)
print("NumPy Array from Tuple:", arr_from_tuple)


