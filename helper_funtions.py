import json
import os


json_file_path = 'userfiles.json'

def append_json(json_file_path, new_data):
    
    if os.path.exists(json_file_path):

        with open(json_file_path, 'r') as file:
            data = json.load(file)

    else:
        data = []

    data.append(new_data)

    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)
    