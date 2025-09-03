import numpy as np

x=np.array([1,2,3])
y=np.array([4,5,6])

print(np.dot(x,y))  # 1*4+2*5+3*6=32
print(np.dot(y,x))     # 32

## OR ##

x@y  # 32