import numpy as np

a=np.array([1,2,3])
b=np.array([[1,2,3],[4,5,6],[7,8,9]])

arr=np.dot(a,b)
print(arr)  # [1*1+2*4+3*7 , 1*2+2*5+3*8 , 1*3+2*6+3*9] = [30 36 42]

#### OR ####

arr=a@b
print(arr)  # [30 36 42]