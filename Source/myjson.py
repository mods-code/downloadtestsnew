import json
import os

def create_info_json(modname, author, desciption,factorio_version):
    info = {
        "name": modname,
        "author": author,
        "desciption": desciption,
        "title": modname,
        "version": "0.0",
        "factorio_version": factorio_version
    }
    json_string = json.dumps(info)
    return json_string

def save_info_json(modname, json_string):
    folder_path = f"mods/{modname}"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    filename = f"{folder_path}/info.json"
    with open(filename, "w") as f:
        f.write(json_string)


def load_info_json(mod_name,file_name):
    json_path = f"mods/{mod_name}/{file_name}"
    json_data = open(json_path,'r')
    json_data2 = json_data.read()
    json_data.close()
    return json_data2


def return_jsonkey(keyname,json_str):
    data = json.loads(json_str)
    out = data[keyname]
    return out

def load_jasonkey(mod_name,file_name,jsonkey):
    return return_jsonkey(jsonkey,load_info_json(mod_name,file_name))