import matplotlib.pyplot as plt

x=['Mon','Tue','Wed','Thu','Fri']
y=[10,20,15,12,30]

plt.plot(x,y)

plt.title('Backery sales this week!')
plt.xlabel('day of the week')
plt.ylabel('sales per day')

plt.show()