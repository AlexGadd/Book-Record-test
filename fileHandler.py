import json

file_name = "data.json"

def load():
    fh = open(file_name,"r")
    data = json.load(fh)
    return data
    fh.close()

def save(arg):
    fh = open(file_name,"w")
    json.dump(arg,fh)
    fh.close
