#Write a NumPy program to test whether each element of a 1D array is also present in a second array..

import numpy as np

arr1=np.array([0,10,20,30,40,50])
arr2=np.array([0,40])

print(np.isin(arr1,arr2))  # Check which elements of arr1 are in arr2

