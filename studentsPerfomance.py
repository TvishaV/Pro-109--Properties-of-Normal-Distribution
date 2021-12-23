import csv
import statistics
import pandas as pd 
import plotly.figure_factory as ff 
import random
import plotly.graph_objects as go

df = pd.read_csv("studentsPerfomance.csv")
data = df["reading score"].tolist()

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)

print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))

std_deviation = statistics.stdev(data)

print("Standard deviation of this data is {}".format(std_deviation))

sd1_start , sd1_end = mean - std_deviation , mean + std_deviation
sd2_start , sd2_end = mean - (2*std_deviation) , mean + (2*std_deviation)
sd3_start , sd3_end = mean - (3*std_deviation) , mean + (3*std_deviation)

fig = ff.create_distplot( [data], ["reading scores"], show_hist=False)

fig.add_trace (go.Scatter (x = [mean, mean], y = [0, 0.17], mode = "lines", name = "mean"))

fig.add_trace (go.Scatter (x = [sd1_start, sd1_start], y = [0, 0.17], mode = "lines", name = "sd1 start"))
fig.add_trace (go.Scatter (x = [sd1_end, sd1_end], y = [0, 0.17], mode = "lines", name = "sd1 end"))

fig.add_trace (go.Scatter (x = [sd2_start, sd2_start], y = [0, 0.17], mode = "lines", name = "sd2 start"))
fig.add_trace (go.Scatter (x = [sd2_end, sd2_end], y = [0, 0.17], mode = "lines", name = "sd2 end"))

list_of_data_within_1_std_deviation = [result for result in data if result > sd1_start and result < sd1_end]
list_of_data_within_2_std_deviation = [result for result in data if result > sd2_start and result < sd2_end]
list_of_data_within_3_std_deviation = [result for result in data if result > sd3_start and result < sd3_end]

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))

fig.show()