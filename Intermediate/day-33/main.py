import requests
from datetime import datetime
LAT = -6.183078
LONG = 35.748161
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# longitude = response.json()['iss_position']['longitude']
# latitude = response.json()['iss_position']['latitude']
#
# position = (longitude, latitude)
# print(position)

parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0,
}

response = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
