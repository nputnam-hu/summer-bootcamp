import json

def get():
  with open("config.json") as json_data:
    d = json.load(json_data)
    json_data.close()
    return d