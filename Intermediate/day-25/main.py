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
print(data['temp'])
