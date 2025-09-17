import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

np.random.seed(42) 

food = np.random.randint(5000, 15000, size=12)
rent = np.random.randint(10000, 20000, size=12)
transport = np.random.randint(2000, 8000, size=12)
entertainment = np.random.randint(1000, 6000, size=12)
shopping = np.random.randint(2000, 10000, size=12)

df = pd.DataFrame({
    "Month": months,
    "Food": food,
    "Rent": rent,
    "Transport": transport,
    "Entertainment": entertainment,
    "Shopping": shopping
})

df["Total"] = df[["Food", "Rent", "Transport", "Entertainment", "Shopping"]].sum(axis=1)

category_avg = df[["Food", "Rent", "Transport", "Entertainment", "Shopping"]].mean()

highest_month = df.loc[df["Total"].idxmax(), "Month"]

print(" Monthly Expenses Data:\n", df)
print("\n Average Expense per Category:\n", category_avg)
print(f"\n Highest Spending Month: {highest_month}")

plt.figure(figsize=(10,5))
plt.bar(df["Month"], df["Total"], color="skyblue")
plt.title("Monthly Total Expenses")
plt.xlabel("Month")
plt.ylabel("Total Expense (₹)")
plt.show()

plt.figure(figsize=(10,6))
for col in ["Food", "Rent", "Transport", "Entertainment", "Shopping"]:
    plt.plot(df["Month"], df[col], marker="o", label=col)
plt.title("Monthly Expense Trends by Category")
plt.xlabel("Month")
plt.ylabel("Expense (₹)")
plt.legend()
plt.show()

plt.figure(figsize=(6,6))
plt.pie(category_avg, labels=category_avg.index, autopct="%1.1f%%", startangle=140)
plt.title("Yearly Expense Distribution by Category")
plt.show()
