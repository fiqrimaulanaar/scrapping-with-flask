import requests

url = requests.get("http://www.floatrates.com/daily/idr.json")
json_data = url.json()

for data in json_data.values():
    print(data["code"])
    print(data["name"])
    print(data["date"])
    print(data["inverseRate"])