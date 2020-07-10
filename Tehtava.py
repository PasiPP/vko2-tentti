import requests
import json


response = requests.get('https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json')
data = response.json()

for items in data['items']:
    print(f'{items["parameter"]}.')

with open("checkpoint.txt", "w") as json_file:
    json.dump(data, json_file, indent=4)
    json_file.write("\n")