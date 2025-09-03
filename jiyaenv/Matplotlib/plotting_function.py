#plt.plot(x,y,color='color_name', linstyle='line_style', linewidth=value, marker='marker symbol', label='label name')

import matplotlib.pyplot as plt

Months=[1,2,3,4]
Sales=[1000,2000,4000,3000]

plt.plot(Months,Sales, color='blue', linestyle='--', linewidth=2, marker='o', label='2025 sales data')
plt.xlabel('Months')
plt.ylabel('Sales per month')
plt.title('Monthly sales data report')
plt.legend(loc='upper left',fontsize=12)#parameters are optional
plt.grid(color='gray',linestyle=':',linewidth=1)#parameters are optional
plt.xlim(1,4)
plt.ylim(0,3000)
plt.xticks([1,2,3,4],['M1','M2','M3','M4'])
plt.show()