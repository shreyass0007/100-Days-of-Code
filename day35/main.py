import requests
MY_LAT=18.521374
MY_LON=73.854507
API_KEY="f1cc06880d866ec1f608a256d8851e1a"
OWM_ENDPOINT="http://api.openweathermap.org/data/2.5/forecast"
PARAMETER={
    "lat":MY_LAT,
    "lon":MY_LON,
    "appid":API_KEY,
    "cnt":4,
}
response=requests.get(OWM_ENDPOINT,params=PARAMETER)
response.raise_for_status()
weather_data=response.json()
#print(weather_data["list"][0]["weather"][0]["id"])
will_rain=False
for hour_data in weather_data["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code) <700:
        wil_rain=True

if will_rain:
    print("Bring an Umbrella")
else:
    print("No Rain Today")

