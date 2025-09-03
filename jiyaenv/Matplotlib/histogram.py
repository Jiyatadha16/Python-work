import matplotlib.pyplot as plt

#plt.hist(data,bins=no_of_bins,color='colorname',edgecolor='black')

score=[45,34,45,67,87,63,56,43,54,32,45]

plt.hist(score,bins=5,color='purple',edgecolor='black')
plt.xlabel('Score range')
plt.ylabel('Number of students')
plt.title('Score distribution of students')
plt.show()