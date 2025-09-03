#### write a NumPy program to find the real and imaginary parts of an array of complex number.

import numpy as np

# Create a NumPy array of complex numbers
complex_arr = np.array([2 + 3j, 4 - 5j, -1 + 6j, -7 - 8j])

# Extract real and imaginary parts
real_part = complex_arr.real
imag_part = complex_arr.imag

print("Complex Array:", complex_arr)
print("Real Part:", real_part)
print("Imaginary Part:", imag_part)

