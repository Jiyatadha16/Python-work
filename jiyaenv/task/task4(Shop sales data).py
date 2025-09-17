import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dates = pd.date_range(start="2025-01-01", end="2025-06-30", freq="D")

np.random.seed(42)  

electronics = np.random.randint(5000, 20000, size=len(dates))
clothing = np.random.randint(2000, 10000, size=len(dates))
groceries = np.random.randint(1000, 7000, size=len(dates))
furniture = np.random.randint(3000, 15000, size=len(dates))

df = pd.DataFrame({
    "Date": dates,
    "Electronics": electronics,
    "Clothing": clothing,
    "Groceries": groceries,
    "Furniture": furniture
})

df["Total_Sales"] = df[["Electronics", "Clothing", "Groceries", "Furniture"]].sum(axis=1)

category_avg = df[["Electronics", "Clothing", "Groceries", "Furniture"]].mean()

best_product = category_avg.idxmax()

highest_day = df.loc[df["Total_Sales"].idxmax(), "Date"]

print("Sales Data (First 5 rows):\n", df.head())
print("\nAverage Sales per Category:\n", category_avg)
print(f"\nBest-Selling Product Overall: {best_product}")
print(f"\nHighest Sales Day: {highest_day}")

plt.figure(figsize=(12,5))
plt.plot(df["Date"], df["Total_Sales"], color="blue")
plt.title("Total Daily Sales Trend (Jan–Jun 2025)")
plt.xlabel("Date")
plt.ylabel("Sales (₹)")
plt.show()

df["Month"] = df["Date"].dt.strftime("%b")
monthly_avg = df.groupby("Month")[["Electronics", "Clothing", "Groceries", "Furniture"]].mean()

monthly_avg.plot(kind="bar", figsize=(10,6))
plt.title("Monthly Average Sales per Category")
plt.xlabel("Month")
plt.ylabel("Average Sales (₹)")
plt.legend(title="Category")
plt.show()

plt.figure(figsize=(6,6))
plt.pie(category_avg, labels=category_avg.index, autopct="%1.1f%%", startangle=140)
plt.title("Category Contribution to Total Sales")
plt.show()

monthly_sum = df.groupby("Month")[["Electronics", "Clothing", "Groceries", "Furniture"]].sum()
monthly_sum.plot(kind="bar", stacked=True, figsize=(10,6))
plt.title("Monthly Sales Breakdown by Category (Stacked)")
plt.xlabel("Month")
plt.ylabel("Total Sales (₹)")
plt.legend(title="Category")
plt.show()
