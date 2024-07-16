import json


with open('userfiles.json', 'r') as file:
    data = json.load(file)
    for items in data:
        print(items['chat_id'])

        