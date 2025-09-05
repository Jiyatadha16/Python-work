import matplotlib.pyplot as plt

#savefig('filename.extension, dpi=value, bbox_inches='tight')

x=[1,2,3,4]
y=[10,20,30,22]

#create plot
plt.plot(x,y, color='blue',marker='o')
plt.title('simple line plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.savefig('line_plot.png', dpi=300, bbox_inches='tight')
plt.show()