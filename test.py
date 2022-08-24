import requests 

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "album/1", {"streams": 10, "name": "Views", "song": "Feels"})
print(response.json())
input()
response = requests.get(BASE + "album/1")
print(response.json())
