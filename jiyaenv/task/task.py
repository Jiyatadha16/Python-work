# Compute and display number of days to reach target, and generate annotated plots.
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Replace ace_tools with pandas for displaying dataframes
import pandas as tools

# Given values (same as your original setup)
platform_daily_reach = 1_800_000  # people reachable per day on Meta
meta_usage_fraction = 0.70        # 70% use Meta
target_reach_fraction_of_meta_users = 0.80  # want to reach 80% of the meta-using pool
views_per_100_inr = 4800
cost_unit_inr = 100

# Monetization
revenue_per_1m_downloads_inr = 5.0
revenue_per_download_inr = revenue_per_1m_downloads_inr / 1_000_000  # INR per single download

# Conversion: of the reached audience, 20% will download
download_conversion_fraction = 0.20

# Assumption about daily ad spend (chosen baseline)
daily_budget_inr = 100.0  # change this to simulate other daily budgets

# Derived values
meta_users_pool = platform_daily_reach * meta_usage_fraction
target_audience = meta_users_pool * target_reach_fraction_of_meta_users

impressions_per_inr = views_per_100_inr / cost_unit_inr
daily_impressions = daily_budget_inr * impressions_per_inr

# Days required (ceil to reach at least target)
days_to_reach = int(np.ceil(target_audience / daily_impressions))

# Downloads expected (20% of reached audience)
expected_downloads = target_audience * download_conversion_fraction

# Revenue from those downloads
total_revenue_inr = expected_downloads * revenue_per_download_inr

# Revenue if the same campaign performance repeats daily/monthly/yearly
daily_revenue_repeat = (daily_impressions * download_conversion_fraction) * revenue_per_download_inr
monthly_revenue_repeat = daily_revenue_repeat * 30
yearly_revenue_repeat = daily_revenue_repeat * 365

# Prepare summary dataframe with days included
summary = {
    "meta_users_pool": [meta_users_pool],
    "target_audience": [target_audience],
    "daily_impressions_with_{}INR".format(int(daily_budget_inr)): [daily_impressions],
    "days_to_reach_target": [days_to_reach],
    "expected_downloads_from_target": [expected_downloads],
    "total_revenue_inr_from_target": [total_revenue_inr],
    "daily_revenue_repeat_inr": [daily_revenue_repeat],
    "monthly_revenue_repeat_inr": [monthly_revenue_repeat],
    "yearly_revenue_repeat_inr": [yearly_revenue_repeat],
}
df_summary = pd.DataFrame(summary)

# Time series DataFrame with Day and Cumulative Reach
days = np.arange(1, days_to_reach + 1)
cumulative_reach = np.minimum(days * daily_impressions, target_audience)
ts_df = pd.DataFrame({"Day": days, "Cumulative Reach": cumulative_reach})

# Display dataframe using pandas' built-in functionality
print("INAI_Marketing_Summary_With_Days")
print(df_summary)
tools.display_dataframe_to_user("INAI_Marketing_Summary_With_Days", df_summary)

# Print number of days explicitly
print(f"Number of days to reach {int(100*target_reach_fraction_of_meta_users)}% of Meta users (target audience = {int(target_audience):,}): {days_to_reach} days")

# Create outputs folder and save files
out_dir = os.path.join(os.getcwd(), "outputs")
os.makedirs(out_dir, exist_ok=True)
summary_csv = os.path.join(out_dir, "INAI_Marketing_Summary_with_days.csv")
ts_csv = os.path.join(out_dir, "Cumulative_Reach_Over_Days_with_days.csv")
df_summary.to_csv(summary_csv, index=False)
ts_df.to_csv(ts_csv, index=False)

# Plot 1: Revenue projection bar chart (annotate with days_to_reach info)
labels = ["Daily (repeat)", "Monthly (repeat)", "Yearly (repeat)"]
values = [daily_revenue_repeat, monthly_revenue_repeat, yearly_revenue_repeat]

fig1, ax1 = plt.subplots(figsize=(8,5))
ax1.bar(labels, values)
ax1.set_title("Projected INAI Revenue (if same campaign performance repeats)")
ax1.set_ylabel("INR")
# annotate days info on the plot
ax1.text(0.5, max(values)*0.5, f"Days to reach target: {days_to_reach} days", 
         ha='center', va='center', fontsize=10, bbox=dict(boxstyle="round", facecolor="white", alpha=0.7))
plt.tight_layout()
revenue_png = os.path.join(out_dir, "revenue_projection_with_days.png")
fig1.savefig(revenue_png, dpi=300)
plt.show()
# Display dataframe using pandas' built-in functionality
print("Cumulative_Reach_Over_Days")
print(ts_df)

# Display cumulative reach table
tools.display_dataframe_to_user("Cumulative_Reach_Over_Days", ts_df)

# Plot 2: Cumulative reach vs days with vertical line at days_to_reach and annotation
fig2, ax2 = plt.subplots(figsize=(10,4))
ax2.plot(days, cumulative_reach)
ax2.set_xlabel("Day")
ax2.set_ylabel("Cumulative Reach (people)")
ax2.set_title(f"Cumulative Reach vs Days (daily budget = {int(daily_budget_inr)} INR)")
ax2.grid(True)
# vertical line at target day and annotation
ax2.axvline(days_to_reach, linestyle='--', linewidth=1)
ax2.text(days_to_reach, target_audience*0.05, f" Target reached\n {days_to_reach} days", 
         rotation=0, va='bottom', ha='left', bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))
plt.tight_layout()
reach_png = os.path.join(out_dir, "cumulative_reach_with_days.png")
fig2.savefig(reach_png, dpi=300)
plt.show()
plt.close(fig2)

# Print saved file info
print("\nSaved files:")
print(" -", summary_csv)
print(" -", ts_csv)
print(" -", revenue_png)
print(" -", reach_png)

# Also return key numeric result for programmatic use
{"days_to_reach": days_to_reach, "summary_csv": summary_csv, "ts_csv": ts_csv, "revenue_png": revenue_png, "reach_png": reach_png}

