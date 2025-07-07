import requests
MY_LAT=18.521374
MY_LON=73.854507
API_KEY="f1cc06880d866ec1f608a256d8851e1a"
OWM_ENDPOINT="http://api.openweathermap.org/data/2.5/forecast"
PARAMETER={
    "lat":MY_LAT,
    "lon":MY_LON,
    "appid":API_KEY,
}
response=requests.get(OWM_ENDPOINT,params=PARAMETER)
print(response.json())

