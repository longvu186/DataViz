import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from pandas import read_excel
import json
from sys import stdout


# Show loading percent
def loading(value, data_list):
    stdout.write('\r')
    stdout.write('{}%'.format(round(value / len(data_list) * 100)))


# Load file
with open('Pie chart.json', 'r') as json_file:
    data_file = json.load(json_file)

data_frame = read_excel('Pie chart.xlsx')

# Handle data
time = list(data_frame['Time'])
data_frame.drop(columns='Time', inplace=True)
labels = list(data_frame)
raw_data = data_frame.values.tolist()

title = data_file.get('title')
colors = data_file.get('colors')
font_size = data_file.get('font_size')
font_name = data_file.get('font_name')
if font_name == '':
    font_name = None
resolution = data_file.get('resolution')
transparent = data_file.get('transparent')
data_interpolation = data_file.get('data_interpolation')


# Interpolate data for smooth animation
def interpolate_lists_data(input_list, input_num):
    list_transpose = np.transpose(input_list)
    interpolated_data_transpose = []
    for row in list_transpose:
        interpolated_list = [row[0]]
        for number in range(1, len(row)):
            interpolated_list = interpolated_list + list(np.linspace(row[number - 1], 
                                                                     row[number], 
                                                                     num=input_num)[1:])
        interpolated_data_transpose.append(interpolated_list)
    output_data = np.transpose(interpolated_data_transpose)
    return output_data


smooth_data = interpolate_lists_data(raw_data, data_interpolation)

time_interpolated = []
for item in time:
    time_interpolated = time_interpolated + [item for i in range(data_interpolation-1)]

# Plot the chart
fig, ax = plt.subplots(figsize=(resolution[0]/100, resolution[1]/100))

# Create animation


def update(num):
    ax.clear()
    ax.axis('equal')
    sizes = [i/sum(smooth_data[num])*100 for i in smooth_data[num]]
    ax.pie(sizes,
           labels=labels,
           autopct='%1.1f%%',
           colors=colors,
           explode=[0.05 for i in range(len(sizes))],
           textprops={'fontsize': font_size,
                      'fontname': font_name}
           )
    ax.set_title(time_interpolated[num], pad=0)
    loading(num, smooth_data)


ani = animation.FuncAnimation(fig, update, frames=len(smooth_data),
                              interval=20)

if transparent == "true":
    ani.save('output.mov',
             codec="png",
             dpi=100,
             bitrate=-1,
             savefig_kwargs={'transparent': True,
                             'facecolor': 'none'})
else:
    ani.save('output.mp4')
plt.show()
