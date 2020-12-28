import pickle

file_name = "data.pkl"

def load():
    open_file = open(file_name,"rb")
    loaded_list = pickle.load(open_file)
    return loaded_list
    open_file.close()

def save(arg):
    open_file = open(file_name,"wb")
    pickle.dump(arg, open_file)
    open_file.close