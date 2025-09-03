import numpy as np

vector1=np.array([1,2,3])
vector2=np.array([4,5,6])

print("vactor addition:",vector1+vector2)
print("\nvactor multiplication:",vector1*vector2)
print("\nDot product:",np.dot(vector1,vector2))
angle=np.arccos(np.dot(vector1,vector2)/(np.linalg.norm(vector1)*np.linalg.norm(vector2)))
print("\nAngle between two vectors in radians:",angle)

