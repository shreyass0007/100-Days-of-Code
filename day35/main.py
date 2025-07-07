import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()
MY_LAT=18.521374
MY_LON=73.854507
OWM_ENDPOINT = os.getenv("OWM_ENDPOINT")
API_KEY = os.getenv("API_KEY")
account_sid =os.getenv("account_sid")
auth_token = os.getenv("auth_token")
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
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today.Rember to bring an ☔",
        from_="twilio Phone number",
        to="the no you mant to send sms",
        )
    
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="No Rain Today",
        from_="twilio Phone number",
        to="the no you mant to send sms",
        )

print(message.status)