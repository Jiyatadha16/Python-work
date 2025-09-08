import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('jiyaenv/Matplotlib/Examples/netflix_practice_200.csv')

df=df.dropna(subset=['Title','Type','Release Year','Rating','Duration','Country','Genre'])

types_count=df['Type'].value_counts()
plt.figure(figsize=(8,5))
plt.bar(types_count.index, types_count.values, color=['blue','orange'])
plt.title('Number of Movies and TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('netflix_types_count.png') 
plt.show()

rating_count=df['Rating'].value_counts()
plt.figure(figsize=(10,6))
plt.pie(rating_count.values, labels=rating_count.index, autopct='%1.1f%%', startangle=140)
plt.title('percentage of content by Rating on Netflix')
plt.tight_layout()
plt.savefig('content_rating_pie.png')
plt.show()