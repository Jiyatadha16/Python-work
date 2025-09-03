import numpy as np

x=np.array([1,2,3])
a=np.array([[1,2,3],[4,5,6]])
print(a)

arr=np.dot(a,x)  
print(arr)  # [1*1+2*2+3*3 , 4*1+5*2+6*3] = [14 32]