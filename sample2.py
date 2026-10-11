import requests

url = "https://static-assets-web.flixcart.com/www/linchpin/batman-returns/codes.json"

payload = {
    "title": "Data Engineer",
    "body": "Learning APIs",
    "userId": 1
}

response = requests.get(url)
r=response.json()
c=0
for i in r:
    if i['fullCountryName'].startswith('Saint'):
        print(i)
        print('==================================================')
        c=c+1

print(f'count of saint is {c}')
#print(response.json())
