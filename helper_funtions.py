import json
import base64
import os


json_file_path = 'userfiles.json'

def append_json(new_data: dict, json_file_path: str ="userfiles.json"):
    
    if os.path.exists(json_file_path):

        with open(json_file_path, 'r') as file:
            data = json.load(file)

    else:
        data = []

    data.append(new_data)

    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)

def find_file(file_unique: str) -> str:

    with open('userfiles.json', 'r') as jsonfile:
        files: json = json.load(jsonfile)

        for file in files:
            if file['file_unique'] == file_unique:
                return file['file_id']
# hello why is this so slow and I am typing slower than my grandma

        