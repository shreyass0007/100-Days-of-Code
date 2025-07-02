import requests
import datetime as dt
MY_LAT=40.7483
MY_LNG=-73.9846
parameters={
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0,
}
reponse=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
reponse.raise_for_status()
data=reponse.json()
sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset=data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunset)
print(sunrise)

time_now=dt.datetime.now()
print(time_now.hour)
