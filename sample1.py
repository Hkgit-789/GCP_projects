import requests
import json
url="https://jsonplaceholder.typicode.com/users"

json1=requests.get(url)
json2=json1.json()
print(json1)
print(json2)

with open("users.json", "w") as f:
    json.dump(json2, f, indent=10)

print("File Saved")

print(json.dumps(json2, indent=10))

