#fig, ax= plt.subplots(nrows, ncols, figsize=(width,height))

import matplotlib.pyplot as plt

fig, ax=plt.subplots(1,2, figsize=(10,5))

x=[1,2,3,4,5]
y=[10,20,15,30,12]

ax[0].plot(x,y)
ax[0].set_title('Line chart')

ax[1].bar(x,y)
ax[1].set_title('Bar chart')

#fig, ax=plt.subplots(2,1, sharex=True)

plt.show()