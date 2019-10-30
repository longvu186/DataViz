from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import ticker
from pandas import read_excel
from scipy import stats
from Libraries.Data_viz_lib import DataVisualization as DV


class BarChartRaceClass(DV):
    title = None
    time_text_color = None
    value_format = None
    transparent_background = None
    floating_point = None
    data_interpolation = None
    fps = None
    font_size = None
    colors = None
    labels = None

    def handle_data(self):

        # Get data
        data_frame = read_excel('VizModules/BarChartRace/BarChartRace.xlsx')
        self.colors = list(data_frame.iloc[0][1:])
        data_frame.drop([0], axis=0, inplace=True)
        time = list(data_frame['Time'])
        data_frame.drop(columns='Time', inplace=True)
        self.labels = list(data_frame)
        data = data_frame.values.tolist()

        # Get data ranking
        data_rank = []
        for item in data:
            rank_list = list(stats.rankdata(item, method='ordinal'))
            highest_rank = max(rank_list)
            for index, rank in enumerate(rank_list):
                rank_list[index] = rank + (10-highest_rank)
            for index, rank in enumerate(rank_list):
                if rank <= 0:
                    rank_list[index] = rank - 1
            data_rank.append(rank_list)

        # Interpolate data
        self.time_interpolated = []
        for item in time:
            self.time_interpolated = self.time_interpolated + [item for i in range(self.data_interpolation-1)]
        self.data_interpolated = DV.interpolate_lists_data(data, self.data_interpolation)
        self.data_rank_interpolated = DV.interpolate_lists_data(data_rank, self.data_interpolation)

        # Animate data
        self.fig, self.ax = plt.subplots(figsize=[19.20, 10.80])
        self.min_rank = min(self.data_rank_interpolated[0])
        self.max_rank = max(self.data_rank_interpolated[0])
        self.categories_count = len(self.data_rank_interpolated[0])

    def update(self, num):
        self.ax.clear()
        self.ax.tick_params(length=0, labelsize=self.font_size)
        plt.box(False)
        plt.grid(True, axis='x', color='#bfbfbf')
        plt.barh(self.data_rank_interpolated[num],
                 self.data_interpolated[num],
                 height=0.5,
                 color=self.colors,
                 zorder=3)
        max_value = float(max(self.data_interpolated[num]))
        plt.yticks(range(int(self.min_rank), int(self.max_rank)))
        plt.yticks(self.data_rank_interpolated[num], self.labels)
        self.ax.tick_params(axis='y', which='major', pad=15)
        plt.ticklabel_format(axis='x', style='plain')
        self.ax.set_xticks(self.ax.get_xticks()[::2])
        self.ax.get_xaxis().set_major_formatter(
            ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
        if self.categories_count < 10:
            plt.axis([0, max_value*1.1, 10-self.categories_count, 11])
        else:
            plt.axis([0, max_value*1.1, 0, 11])
        # Time label
        self.ax.text(x=max_value*0.8,
                     y=10-self.categories_count+0.25*self.categories_count,
                     s=self.time_interpolated[num],
                     fontsize=50,
                     fontweight='bold',
                     color=self.time_text_color)
        # Value label
        for index, value in enumerate(self.data_interpolated[num]):
            self.ax.text(x=max_value/50+value,
                         y=self.data_rank_interpolated[num][index],
                         s=self.value_format.format('{:,}'.format(int(round(value, self.floating_point)))),
                         verticalalignment='center',
                         fontsize=self.font_size)
        plt.subplots_adjust(left=0.15)
        DV.loading(num, self.data_rank_interpolated)

    def export(self):
        self.handle_data()
        ani = animation.FuncAnimation(self.fig, self.update, frames=len(self.data_rank_interpolated),
                                      interval=1000 / self.fps)
        DV.save_ani(ani, self.transparent_background)

    def preview(self):
        self.handle_data()
        DV.preview(self.update)
