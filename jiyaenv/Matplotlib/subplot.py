import matplotlib.pyplot as plt

#plt.subplot(nrows, ncols, index)

x=[1,2,3,4,5]
y=[10,20,15,25,30]

plt.subplot(1,2,1)
plt.plot(x,y)
plt.title('Line chart')

plt.subplot(1,2,2)
plt.plot(x,y)
plt.title('Bar chart')

plt.tight_layout()
plt.show()

