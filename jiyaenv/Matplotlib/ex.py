import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button, Slider

# 1. Line Chart Animation
def line_chart_animation():
    fig, ax = plt.subplots(figsize=(6, 5))
    x, y = [], []
    line, = ax.plot(x, y, 'b-', lw=2)
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 100)
    ax.set_title("Line Chart Animation")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")

    def animate(frame):
        x.append(frame)
        y.append(np.random.randint(0, 100))
        if len(x) > 50:
            x.pop(0)
            y.pop(0)
        line.set_data(x, y)
        return line,

    anim = animation.FuncAnimation(fig, animate, frames=100, interval=200, blit=True, repeat=True)

    # Add controls
    def toggle_pause(event):
        if anim.running:
            anim.event_source.stop()
        else:
            anim.event_source.start()
        anim.running = not anim.running

    ax_button = plt.axes([0.4, 0.05, 0.15, 0.04])
    button = Button(ax_button, 'Pause/Play')
    button.on_clicked(toggle_pause)

    def update_speed(val):
        anim.event_source.interval = val

    ax_slider = plt.axes([0.2, 0.05, 0.15, 0.04])
    slider = Slider(ax_slider, 'Speed (ms)', 50, 1000, valinit=200)
    slider.on_changed(update_speed)

    anim.running = True
    plt.show()

# 2. Bar Chart Animation
def bar_chart_animation():
    fig, ax = plt.subplots(figsize=(6, 5))
    categories = ['A', 'B', 'C', 'D', 'E']
    final_heights = [15, 30, 45, 10, 25]
    bars = ax.bar(categories, [0] * len(categories), color='skyblue')
    ax.set_title("Bar Chart Animation")
    ax.set_ylim(0, max(final_heights) + 10)

    def animate(frame):
        for i, bar in enumerate(bars):
            bar.set_height(final_heights[i] * min(frame / 20, 1))
        return bars

    anim = animation.FuncAnimation(fig, animate, frames=100, interval=200, blit=False, repeat=True)

    # Add controls
    def toggle_pause(event):
        if anim.running:
            anim.event_source.stop()
        else:
            anim.event_source.start()
        anim.running = not anim.running

    ax_button = plt.axes([0.4, 0.05, 0.15, 0.04])
    button = Button(ax_button, 'Pause/Play')
    button.on_clicked(toggle_pause)

    def update_speed(val):
        anim.event_source.interval = val

    ax_slider = plt.axes([0.2, 0.05, 0.15, 0.04])
    slider = Slider(ax_slider, 'Speed (ms)', 50, 1000, valinit=200)
    slider.on_changed(update_speed)

    anim.running = True
    plt.show()

# 4. Scatter Chart Animation
def scatter_chart_animation():
    fig, ax = plt.subplots(figsize=(6, 5))
    x = np.random.rand(50)
    y = np.random.rand(50)
    scatter = ax.scatter([], [], c='blue', s=100, alpha=0.6)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("Scatter Chart Animation")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")

    def animate(frame):
        scatter.set_offsets(np.c_[x[:frame], y[:frame]])
        return scatter,

    anim = animation.FuncAnimation(fig, animate, frames=50, interval=200, blit=True, repeat=True)

    # Add controls
    def toggle_pause(event):
        if anim.running:
            anim.event_source.stop()
        else:
            anim.event_source.start()
        anim.running = not anim.running

    ax_button = plt.axes([0.4, 0.05, 0.15, 0.04])
    button = Button(ax_button, 'Pause/Play')
    button.on_clicked(toggle_pause)

    def update_speed(val):
        anim.event_source.interval = val

    ax_slider = plt.axes([0.2, 0.05, 0.15, 0.04])
    slider = Slider(ax_slider, 'Speed (ms)', 50, 1000, valinit=200)
    slider.on_changed(update_speed)

    anim.running = True
    plt.show()

# 5. Histogram Animation
def histogram_animation():
    fig, ax = plt.subplots(figsize=(6, 5))
    data = np.random.randn(1000)
    bins = np.linspace(-4, 4, 20)
    hist = ax.hist([], bins=bins, color='skyblue', edgecolor='black')
    ax.set_title("Histogram Animation")
    ax.set_xlim(-4, 4)
    ax.set_ylim(0, 150)
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")

    def animate(frame):
        ax.clear()
        subset = data[:frame * 5]
        ax.hist(subset, bins=bins, color='skyblue', edgecolor='black')
        ax.set_xlim(-4, 4)
        ax.set_ylim(0, 150)
        ax.set_title("Histogram Animation")
        ax.set_xlabel("Value")
        ax.set_ylabel("Frequency")
        return ax.patches

    anim = animation.FuncAnimation(fig, animate, frames=100, interval=200, blit=False, repeat=True)

    # Add controls
    def toggle_pause(event):
        if anim.running:
            anim.event_source.stop()
        else:
            anim.event_source.start()
        anim.running = not anim.running

    ax_button = plt.axes([0.4, 0.05, 0.15, 0.04])
    button = Button(ax_button, 'Pause/Play')
    button.on_clicked(toggle_pause)

    def update_speed(val):
        anim.event_source.interval = val

    ax_slider = plt.axes([0.2, 0.05, 0.15, 0.04])
    slider = Slider(ax_slider, 'Speed (ms)', 50, 1000, valinit=200)
    slider.on_changed(update_speed)

    anim.running = True
    plt.show()

# Run all animations
line_chart_animation()
bar_chart_animation()
scatter_chart_animation()
histogram_animation()
