#Given a 1D array, negative all elements which are between 3 and 8 , in place… 

import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr)
a = np.arange(10)
a[(3<a) & (a<8)] *= -1
print(a)

