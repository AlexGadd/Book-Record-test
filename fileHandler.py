import pickle

file_name = "data.json"

def load():
    open_file = open(file_name,"r").read
    return open_file
    open_file.close()

def save(arg):
    open_file = open(file_name,"w")
    open_file.dump(arg)
    open_file.close