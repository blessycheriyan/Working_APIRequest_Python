import requests
import pandas as pf

url = 'https://rickandmortyapi.com/api/'
endpoint = 'character'

def main_request(url, endpoint, x):
    response = requests.get(url + endpoint +f'?page={x}')
    return response.json()

def get_pages(response):
    return response['info']['pages']

def parse_json(response):
    charlist =[]
    for item in response['results']:
        # print(item['name'],len(item['episode']))
        char ={
            'id':item['id'],
            'name':item['name'],
            'no_episode':len(item['episode']),
        }
        charlist.append(char)
    return charlist
mainlist =[]    
data = main_request(url, endpoint,2)
# print(get_pages(data))
# print(parse_json(data))
for x in range(1,get_pages(data)+1):
    print(x)
    mainlist.extend(parse_json(main_request(url, endpoint,x)))
    
# print(len(mainlist))  
    
df = pf.DataFrame(mainlist)
# print(df.head(),df.tail())
df.to_csv('charlist.csv',index=False)
    
    
    