# with open(r'Depth_python\DAY25_Pandas_and_CSV\weather_data.csv',mode='rt') as data:
#     # data.read()
#     list_named_data = data.readlines()
#     print(list_named_data)

# import csv

# with open(r'Depth_python\DAY25_Pandas_and_CSV\weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for index, row in enumerate(data):
#         _temp = row[1]
#         if _temp != "temp":
#             temperatures.append(int(_temp))
#     print(temperatures)

# import pandas

# data = pandas.read_csv(r'Depth_python\DAY25_Pandas_and_CSV\weather_data.csv')
# # data_dict = data.to_dict()

# temp_list = data['temp'].to_list()

# average_temp = 0
# average_temp = round(sum(temp_list)/len(temp_list),2)

# print(data['temp'].mean()) # get average
# print(data['temp'].max()) # get max value of temperatures

#Get data in columns
# print(data['condition']) #or can call like down below
# data.condition

#Get data in row
# result = data[data.day == 'Tuesday'] #data look trhough on the column 'monday' and returning row value
# print(result)

# result = data[data['temp'] == data['temp'].max()]
# print(result)

# result = data[data.day == 'Monday'] #get series data from specific row
# fahrenheit = round(result.temp * 1.8 + 32, 2)
# print(fahrenheit)

#Create data frame from scratch
# data_dict = {
#     "students":['Amy','James','Syarif'],
#     "scores":[76,56,65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv(r'Depth_python\DAY25_Pandas_and_CSV\new_data.csv')
# print(data)

# Squirrel data
import pandas

data_file = pandas.read_csv(r'Depth_python\DAY25_Pandas_and_CSV\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur_color = data_file['Primary Fur Color'].tolist()
print(fur_color)
total_gray = 0
total_red = 0
total_black = 0

for i,color in enumerate(fur_color):
    if color == 'Gray':
        total_gray += 1
    if color == 'Cinnamon':
        total_red +=1
    if color == 'Black':
        total_black +=1

print(f"grey: {total_gray}")
print(f"red: {total_red}")
print(f"black: {total_black}")

data_dict = {
    "Fur Color":['grey','red','black'],
    "Count":[total_gray,total_red,total_black]
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv(r'Depth_python\DAY25_Pandas_and_CSV\squirrel_count.csv')
        