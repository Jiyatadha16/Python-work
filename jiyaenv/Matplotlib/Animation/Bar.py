import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set style for better-looking plots
plt.style.use('seaborn-v0_8')

# Create a figure and axis
fig, ax = plt.subplots()

# Generate sample data for the animation
data = np.cumsum(np.random.randn(100))  # Example: cumulative sum of random numbers

def animate_function(frame):
    # Clear previous plot data
    ax.clear()

    # Get data for current frame
    current_data = data[:frame+1]

    # Plot current data
    ax.plot(current_data)

    # Set labels, title, etc.
    ax.set_title(f'Frame {frame}')

# Create animation
anim = animation.FuncAnimation(fig, animate_function, frames=len(data),
                              interval=100, repeat=True)
# Create sample sales data
dates = pd.date_range('2023-01-01', periods=100, freq='D')
products = ['Product A', 'Product B', 'Product C', 'Product D']

# Generate sample data
data = []
for date in dates:
    for product in products:
        sales = random.randint(50, 200) + random.randint(-20, 20)
        profit = sales * random.uniform(0.2, 0.4)
        data.append({
            'Date': date,
            'Product': product,
            'Sales': sales,
            'Profit': profit,
            'Units': random.randint(10, 50)
        })

df = pd.DataFrame(data)
df.to_csv('sample_data.csv', index=False)
print("Sample data created and saved to 'sample_data.csv'")
print(df.head())

def create_bar_animation():
    # Read data
    df = pd.read_csv('sample_data.csv')
    df['Date'] = pd.to_datetime(df['Date'])

    # Group by date and product for cumulative sales
    df_sorted = df.sort_values('Date')
    df_sorted['Cumulative_Sales'] = df_sorted.groupby('Product')['Sales'].cumsum()

    # Get unique dates
    dates = sorted(df['Date'].unique())
    products = df['Product'].unique()

    # Create figure
    fig, ax = plt.subplots(figsize=(12, 8))

    # Colors for bars
    colors = plt.cm.viridis(np.linspace(0, 1, len(products)))

    def animate(frame):
        ax.clear()

        # Get data for current date
        current_date = dates[frame]
        current_data = df_sorted[df_sorted['Date'] == current_date]

        if not current_data.empty:
            # Get cumulative sales for each product up to current date
            cumulative_data = df_sorted[df_sorted['Date'] <= current_date].groupby('Product')['Sales'].sum().reset_index()

            # Create bar chart
            bars = ax.bar(cumulative_data['Product'], cumulative_data['Sales'],
                         color=colors, alpha=0.8, edgecolor='black', linewidth=1)

            # Add value labels on bars
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                       f'${height:,.0f}', ha='center', va='bottom', fontweight='bold')

        # Styling
        ax.set_title(f'Cumulative Sales by Product - {current_date.strftime("%Y-%m-%d")}',
                    fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Products', fontsize=12)
        ax.set_ylabel('Cumulative Sales ($)', fontsize=12)

        # Set consistent y-axis limit
        max_sales = df_sorted.groupby('Product')['Sales'].sum().max()
        ax.set_ylim(0, max_sales * 1.1)

        # Grid and styling
        ax.grid(True, axis='y', alpha=0.3)
        ax.set_axisbelow(True)
        plt.xticks(rotation=45)
        plt.tight_layout()

    # Create animation
    anim = animation.FuncAnimation(fig, animate, frames=len(dates),
                                  interval=300, repeat=True, blit=False)

    plt.show()
    return anim

# Run the animation
bar_anim = create_bar_animation()
