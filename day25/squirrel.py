import pandas as pd
df=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
greay_squirrel=len(df[df["Primary Fur Color"]=="Gray"])
red_squirrel=len(df[df["Primary Fur Color"]=="Cinnamon"])
black_squirrel=len(df[df["Primary Fur Color"]=="Black"])

dict={"Fur color":['Gray','Cinnamon','Black'],
      "count":[greay_squirrel,red_squirrel,black_squirrel]
      }
data=pd.DataFrame(dict)
data.to_csv("NYC_Squirrelcount.csv")