import requests
from twilio.rest import Client
import os
# api_key = os.environ.get("OWM_API_KEY")
api_key = "fc4e0aab80fd57fa623f9ba1b10a6440"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

# auth_token = "4267b5b57b2e3eb9821eba98e0c67fcb"
auth_token = os.environ.get("AUTH_TOKEN")
account_sid = "AC2ba470f94f74272e426b5ee8350d6804"

if auth_token is None:
    print("AUTH_TOKEN environment variable not found")
else:
    print("AUTH_TOKEN:", auth_token)

# parameters = {
#     "lat": 45.464203,
#     "lon": 9.189982,
#     "appid": api_key,
# }
# response = requests.get(url=OWM_endpoint, params=parameters)
# response.raise_for_status()
# weather_data = response.json()
#
# will_rain = False
# for i in range(0, 40):
#     condition_code = weather_data["list"][i]["weather"][0]["id"]
#     if condition_code < 700:
#         will_rain = True
#
# if will_rain:
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#         body="It's going to rain remember to bring an Umbrella",
#         from_='+18156621374',
#         to='+255767059116'
#     )
#     print(message.status)
