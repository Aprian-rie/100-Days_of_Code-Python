import requests
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
# What this code does is that it raises an exception whenever it doesn ot succeed depending on
# the response code number

#Get hold of the actual data
data = response.json()
# This returns our data in json format
print(data)