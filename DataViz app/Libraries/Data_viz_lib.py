# Library for data visualization - Data_viz_lib
from abc import abstractmethod
import numpy as np
from sys import stdout
from matplotlib import pyplot as plt


class DataVisualization:
    @staticmethod
    def loading(value, data_list):
        stdout.write('\r')
        stdout.write('{}%'.format(round(value / len(data_list) * 100)))

    @staticmethod
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

    @staticmethod
    def save_ani(ani, transparent_background):
        if transparent_background:
            ani.save('output.mov',
                     codec="png",
                     dpi=100,
                     bitrate=-1,
                     savefig_kwargs={'transparent': True,
                                     'facecolor': 'none'})
        else:
            ani.save('output.mp4')

    @abstractmethod
    def update(self):
        pass

    @staticmethod
    def preview(update):
        update(1)
        plt.show()







