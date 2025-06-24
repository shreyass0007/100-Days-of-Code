# with open("D:/CODEING/100 days of python/day25/weather_data - Sheet1.csv") as word:
#     print(word.readlines())

# import csv
# with open("D:/CODEING/100 days of python/day25/weather_data - Sheet1.csv") as data_file:
#     data=csv.reader(data_file)
#     temperature=[]
#     for row in data:
#         print(row)
#         if row[1]!="temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas as pd
df=pd.read_csv("D:/CODEING/100 days of python/day25/weather_data - Sheet1.csv")
# print(type(df["temp"]))

# data_dict=df.to_dict()
# print(data_dict)

# temp_list=df["temp"].to_list()
# print(temp_list)
# # avg=sum(temp_list)/len(temp_list)
# # print(avg)

# print(df["temp"].mean())
# print(df["temp"].max())

# #Get Data in colums
# print(df["condition"])
# print(df.condition)

#Get data in rows
print(df[df.day=="Monday"])
print(df.temp==df["temp"].max())

#create Dataframe form scractch

data_dict={
    "students":["amy","James","angela"],
    "scores":[76,56,65]
}
data=pd.DataFrame(data_dict)
#creating csv files
data.to_csv("new_Data.csv")
print(data)