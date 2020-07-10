from pprint import pprint

import requests
import json


response = requests.get('https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json')
data = response.json()
pprint(data)
print(data['items'][0]['parameter'])

pprint(data)
data['items'][0]['parameter']

for items in data['items']:
    print(f'{items["parameter"]}. "\n" {items["number"]}.')

with open('checkpoint.txt', 'w') as json_file:
    json.dump(data, json_file)