import requests

url = "https://httpbin.org/delay/1"

response = requests.get(url, timeout= 12)
response_json = response.json()

print(response.text)

    