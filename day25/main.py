# with open("D:/CODEING/100 days of python/day25/weather_data - Sheet1.csv") as word:
#     print(word.readlines())

import csv
with open("D:/CODEING/100 days of python/day25/weather_data - Sheet1.csv") as data_file:
    data=csv.reader(data_file)
    temperature=[]
    for row in data:
        print(row)
        if row[1]!="temp":
            temperature.append(int(row[1]))
    print(temperature)

