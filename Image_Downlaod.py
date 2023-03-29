import requests

url = 'https://imgs.xkcd.com/comics/python.png'

response = requests.get(url)

# print(dir(response))
# print(response.text)
with open('comic.png', 'wb') as f:
    f.write(response.content)
    