#### write a NumPy program to add a border (filled with 0s)around an existing array..

import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Add zero row at top and bottom
arr_with_rows = np.vstack([
    np.zeros((1, arr.shape[1]), dtype=int),  # top row
    arr,
    np.zeros((1, arr.shape[1]), dtype=int)   # bottom row
])

# Add zero column at left and right
bordered_arr = np.hstack([
    np.zeros((arr_with_rows.shape[0], 1), dtype=int),  # left column
    arr_with_rows,
    np.zeros((arr_with_rows.shape[0], 1), dtype=int)   # right column
])

print("Original Array:\n", arr)
print("\nArray with Border:\n", bordered_arr)


