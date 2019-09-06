# Data visualization for Apple sales
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline
import json

# Load file
with open("apple.json", 'r') as apple_json:
    data = json.load(apple_json)
# Save data into variables
title = data.get('title')
list_data = data.get('data')
time = []
sales = []
year = range(2007, 2019)

for item in list_data:
    time.append(item.get("Time"))
    sales.append(item.get("Units"))

time_int = np.array(range(len(time)))
sales = np.array(sales)
# Plotting the chart
plt.close('all')
fig, ax = plt.subplots(figsize=(10.80, 7.20))

x_smooth = np.linspace(time_int.min(), time_int.max(), 300)  # smooth line
spl = make_interp_spline(time_int, sales, k=3)
y_smooth = spl(x_smooth)

line, = ax.plot(x_smooth, y_smooth)

# Create animation


def update(num, x, y, line):
    line.set_data(x[:num], y[:num])
    return line,


ani = animation.FuncAnimation(fig, update, len(x_smooth),
                              fargs=[x_smooth, y_smooth, line],
                              interval=200, blit=True)

Writer = animation.FFMpegWriter(fps=30, codec='h264')

plt.title(title)
plt.xticks(range(1, len(sales), 4), year)

# ani.save('test.mp4', writer=Writer)
plt.show()

print(x_smooth, y_smooth)

