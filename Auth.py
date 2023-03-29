import requests

url = "https://httpbin.org/basic-auth/bless/abc"

response = requests.get(url, auth = ('bless','abc'))
response_json = response.json()

print(response.text)

    