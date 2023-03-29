import requests

url = 'https://rickandmortyapi.com/api/'
endpoint = 'character'

response = requests.get(url+ endpoint)
response_json = response.json()

# print(response_json['info'])
print(response_json['results'][0]['name'])
    
    
    