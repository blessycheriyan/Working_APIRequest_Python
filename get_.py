import requests

payload = {'page': 2,'count':25 }
url = 'https://httpbin.org/get'

response = requests.get(url,params=payload)

print(response.text)

    