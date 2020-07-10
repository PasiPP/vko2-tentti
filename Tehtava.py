import requests
import json
import boto3
import logging
from botocore.exceptions import ClientError

response = requests.get('https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json')
data = response.json()

with open("checkpoint.txt", "w") as json_file:
    # json.dump(data, json_file, indent=4)

    for items in data['items']:
        json_file.write(f'{items["parameter"]}.')
        json_file.write("\n")
        print(f'{items["parameter"]}.')

def upload_file(file_name, bucket, object_name=None):

        if object_name is None:
            object_name = file_name

        s3_client = boto3.client('s3')
        try:
            response = s3_client.upload_file(file_name, bucket, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True

upload_file('C:\\Users\\Yoda\\PycharmProjects\\vko2\\checkpoint.txt', 'pasi-checkpoint1', 'checkpoint.txt')