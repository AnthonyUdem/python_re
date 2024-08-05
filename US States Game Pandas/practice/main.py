# with open("weather_data.csv") as weather_data:
#     data_list = weather_data.headlines()
#     print(data_list)

# import csv
# with open("weather_data.csv") as weather_data:
#     data_object = csv.reader(weather_data)
#     temperatures = []
#     for data in data_object:
#         if data[1] != "temp":
#             temperatures.append(data[1])
#     print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
data_dic = data.to_dict()
# print(data_dic)

data_list = data["temp"].to_list()
print(data_list)

# average = round(sum(data_list)/len(data_list), 2)
# print(f"This is the average temperature: {average}")
#
# mean_average = round(data["temp"].mean(), 2)
# print(f"This is the mean average temperature: {mean_average}")
# print(data["temp"].min())
# print(data["temp"].max())

# Get Data in Column
# print(data["condition"])    # you can use this methode
# print(data.condition)       # Or you can use this methode

# Get data in Row
# print(data[data.day == "Monday"])
# print(data[data["day"] == "Sunday"])
# print(data[data.temp == data.temp.max()])
# print(data[data.temp == data.temp.min()])

# monday = data[data.day == "Monday"]

# Create Data frame from scratch
# data_list = {
#     "students": ["Emie", "Bella", "mie"],
#     "score": [76, 56, 65]
# }
#
# print(data_list)
# data_frame = pandas.DataFrame(data_list)
# print(data_frame)

# # data_frame.to_csv("new_data.csv")
#
# Emie = data_frame[data_frame.students == "Emie"]
# print(Emie)
# print(Emie.score)

# central_pack_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240117.csv")
# # -------------------------- method 1 --------------------------
# # fur_colour = central_pack_data["Primary Fur Color"]
# # fur_colour_list = fur_colour.to_list()
# # gray = 0
# # cinnamon = 0
# # black = 0
# # for colours in fur_colour_list:
# #     if colours == "Gray":
# #         gray += 1
# #     elif colours == "Cinnamon":
# #         cinnamon += 1
# #     elif colours == "Black":
# #         black += 1
# # -------------------------- method 1 end --------------------------
# # -------------------------- method 2 --------------------------
# gray = len(central_pack_data[central_pack_data["Primary Fur Color"] == "Gray"])
# cinnamon = len(central_pack_data[central_pack_data["Primary Fur Color"] == "Cinnamon"])
# black = len(central_pack_data[central_pack_data["Primary Fur Color"] == "Black"])
# # -------------------------- method 2 end --------------------------
#
# results = {
#     "fur colour": ["gray", "Cinnamon", "black"],
#     "count": [gray, cinnamon, black]
# }
# # print(results)
#
# results_frame = pandas.DataFrame(results)
# print(results_frame)
# results_frame.to_csv("squirrel_count.csv")
