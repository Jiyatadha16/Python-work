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

def create_scatter_animation():
    # Read data
    df = pd.read_csv('sample_data.csv')
    df['Date'] = pd.to_datetime(df['Date'])

    # Get unique dates
    dates = sorted(df['Date'].unique())
    products = df['Product'].unique()

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # Color map for products
    colors = plt.cm.tab10(np.linspace(0, 1, len(products)))
    color_map = dict(zip(products, colors))

    def animate(frame):
        ax.clear()

        # Get data up to current frame
        current_date = dates[frame]
        current_data = df[df['Date'] <= current_date]

        # Create scatter plot for each product
        for product in products:
            product_data = current_data[current_data['Product'] == product]
            if not product_data.empty:
                ax.scatter(product_data['Sales'], product_data['Profit'],
                          c=[color_map[product]], label=product, alpha=0.7, s=60)

        # Add trend line for all data
        if not current_data.empty:
            z = np.polyfit(current_data['Sales'], current_data['Profit'], 1)
            p = np.poly1d(z)
            x_trend = np.linspace(current_data['Sales'].min(), current_data['Sales'].max(), 100)
            ax.plot(x_trend, p(x_trend), "r--", alpha=0.8, linewidth=2, label='Trend')

        # Styling
        ax.set_title(f'Sales vs Profit Relationship - Up to {current_date.strftime("%Y-%m-%d")}',
                    fontsize=14, fontweight='bold')
        ax.set_xlabel('Sales ($)', fontsize=12)
        ax.set_ylabel('Profit ($)', fontsize=12)
        ax.legend(loc='upper left')
        ax.grid(True, alpha=0.3)

        # Set consistent axis limits
        ax.set_xlim(df['Sales'].min() * 0.9, df['Sales'].max() * 1.1)
        ax.set_ylim(df['Profit'].min() * 0.9, df['Profit'].max() * 1.1)

        plt.tight_layout()

    # Create animation
    anim = animation.FuncAnimation(fig, animate, frames=len(dates),
                                  interval=250, repeat=True, blit=False)

    plt.show()
    return anim

# Run the animation
scatter_anim = create_scatter_animation()
