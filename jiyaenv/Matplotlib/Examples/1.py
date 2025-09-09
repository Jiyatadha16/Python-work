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

movie_df = df[df['Type'] == 'Movie']
movie_df['Duration'] = movie_df['Duration'].str.replace(' min', '').astype(int)

plt.figure(figsize=(10,6))
plt.hist(movie_df['Duration'], bins=30, color='green', edgecolor='black')
plt.title('Distribution of Movie Durations on Netflix')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('movie_duration_distribution.png')
plt.show()

release_year_count = df['Release Year'].value_counts().sort_index()
plt.figure(figsize=(12,6))
plt.plot(release_year_count.index, release_year_count.values, marker='o')
plt.title('Release Year vs Number of shows')
plt.xlabel('Release Year')
plt.ylabel('Number of Shows')
plt.tight_layout()
plt.savefig('release_year_Scatter.png')
plt.show()

country_count = df['Country'].value_counts().head(10)
plt.figure(figsize=(10,6))
plt.barh(country_count.index, country_count.values, color='purple')
plt.title('Top 10 Countries by Number of Shows on Netflix')
plt.xlabel('Number of Shows')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('top_10_countries.png')
plt.show()

content_by_year=df.groupby(['Release Year','Type']).size().unstack().fillna(0)

fig, ax=plt.subplots(1,2,figsize=(12,6))

#first subplot:movies

ax[0].plot(content_by_year.index, content_by_year['Movie'], marker='o', color='blue')
ax[0].set_title('Movies Released Over the Years')
ax[0].set_xlabel('Release Year')
ax[0].set_ylabel('Number of Movies')

#second subplot:tv shows

ax[1].plot(content_by_year.index, content_by_year['TV Show'], marker='o', color='orange')
ax[1].set_title('TV Shows Released Over the Years')
ax[1].set_xlabel('Release Year')
ax[1].set_ylabel('Number of TV Shows')

fig.suptitle('Comparison between Movies and TV Shows Released Over the Years')
plt.tight_layout()
plt.savefig('movies_vs_tvshows.png')
plt.show()