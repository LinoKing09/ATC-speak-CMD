import json 

class misc_data:
    error = False


def load_json(file_name):
    with open(file_name) as json_file:
        datax = json.load(json_file)
        return datax