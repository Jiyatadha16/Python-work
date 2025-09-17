import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

population_7_cities = 108670000  # Total population of 7 cities as per 2025 report
meta_user_percentage = 0.7       # 70% of population Meta use kare
target_audience_percentage = 0.8 # 80% of Meta users target chhe
conversion_rate = 0.2            # 20% of reached audience download kare
income_per_million_downloads = 5 # ₹5 per 1M downloads
daily_budget_inr = 100  # ₹100/day

total_meta_users = population_7_cities * meta_user_percentage
total_target_audience = total_meta_users * target_audience_percentage

impressions_per_100_inr = 4800
impressions_per_day = (daily_budget_inr / 100) * impressions_per_100_inr
days_to_reach_target = int(np.ceil(total_target_audience / impressions_per_day))  # int value mate

downloads = total_target_audience * conversion_rate
income_per_day = (downloads / 1_000_000) * income_per_million_downloads

# Monthly and yearly income
days_in_month = 30
days_in_year = 365
income_per_month = income_per_day * days_in_month
income_per_year = income_per_day * days_in_year

data = {
    'Period': ['Daily', 'Monthly', 'Yearly'],
    'income (₹)': [income_per_day, income_per_month, income_per_year],
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
plt.bar(df['Period'], df['income (₹)'], color=['blue', 'green', 'red'])
plt.title(f'Income for INAI Marketing Campaign (Daily Budget: ₹{daily_budget_inr})')
plt.xlabel('Period')
plt.ylabel('income (₹)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

for i, v in enumerate(df['income (₹)']):
    plt.text(i, v, f"₹{v:,.2f}", ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('income_projection_dynamic.png')
plt.show()

print(f"Days to Reach Target Audience: {days_to_reach_target} days")
print(f"Daily Revenue: ₹{income_per_day:,.2f}")
print(f"Monthly Revenue: ₹{income_per_month:,.2f}")
print(f"Yearly Revenue: ₹{income_per_year:,.2f}")
