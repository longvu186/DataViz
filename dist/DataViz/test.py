from pandas import read_excel
data_frame = read_excel('VizModules/BarChartRace/Bar Chart Race.xlsx')
# Get data
data_frame = read_excel('VizModules/BarChartRace/Bar Chart Race.xlsx')
colors = list(data_frame.iloc[0][1:])
time = list(data_frame['Time'])
data_frame.drop(columns='Time', inplace=True)
data_frame.drop([0], axis=0, inplace=True)
labels = list(data_frame)
data = data_frame.values.tolist()

print(colors)
print(labels)
print(data)