import matplotlib.pyplot as plt

#plt.pie(values, labels=label_list, color=color_list, autopct='%1.1%%')

regions=['South','East','West','North']
revenue=[1000,2000,1500,900]

plt.pie(revenue, labels=regions,autopct='%1.1f%%',colors=['blue','lightgreen','pink','coral'])
plt.title('Revenue contribution by region')
plt.show()
