import json

def load():
    fh = open("data.json","r")
    return fh.read()
    fh.close()

def save(arg):
    fh = open("data.json","w")
    fh.write(json.dumps(arg))
    fh.close
