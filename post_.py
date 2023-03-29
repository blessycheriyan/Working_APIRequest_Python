import requests

payload = {'username': 'james','password':'testing' }
url = 'https://httpbin.org/post'

response = requests.post(url, data=payload)
response_json = response.json()
print(response_json['form'])
print(response_json['form']['username'])
# print(response.text)

    