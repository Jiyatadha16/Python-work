#plt.bar(x,height,color='color_name',width=value,label='label name')
import matplotlib.pyplot as plt

product=['A','B','C','D']
sales=[1000,1500,800,1200]

plt.bar(product,sales,color='orange',label='sales 2025')

plt.xlabel('product')
plt.ylabel('sales')
plt.title('product sale comparision')
plt.legend()
plt.show()