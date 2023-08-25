# with open("226 weather-data.csv", 'r') as data_file:
#     data = data_file.readlines()
#     print(data)
#
# import csv
#
# with open("226 weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     tempertures = []
#     # row horizontal
#
#     for row in data:
#         if row[1] != 'temp':
#             tempertures.append(int(row[1]))
#     print(tempertures)

import pandas

data = pandas.read_csv('226 weather-data.csv')
# print(type(data['temp']))
# print(data.size)

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].tolist()
# print(temp_list)
#
# print(data['temp'].mean())
# print(data['temp'])
# print(data['temp'].max())
#
# condition_column = data.condition
# print(condition_column)

# Get data in A Row
# print(data['condition'][data['condition'] == "Sunny"].size)
# print(data['temp'])
print(data['temp'][data.day == "Monday"])
# print(data[data.temp == data['temp'].max()])
#
# monday = data[data.day == 'Monday']
# # print(monday.condition.)
#
# monday_temp = int(monday.temp.iloc[0])
#
# monday_temp_F = (monday_temp*(9/5)) + 32
#
# print(monday_temp_F)

# data_dict  = {
#     "students": ["Amy", "James", "Angela"],
#     "scores" : [76, 56, 65]
# }
# data2 = pandas.DataFrame(data_dict)
# data2.to_csv("new_data.csv")

# print(data2)