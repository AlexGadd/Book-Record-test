import pickle

# def load():
#     fh = open("data.pkl","r")
#     return fh.read()
#     fh.close()

# def save(arg):
#     fh = open("data.pkl","w")
#     fh.write(pickle.dumps(arg))
#     fh.close

# def save_object(obj):
#     with open("data.pkl", 'wb') as output:  # Overwrites any existing file.
#         pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

sample_list = [1, 2, 3]
file_name = "sample.pkl"

# open_file = open(file_name, "wb")
# pickle.dump(sample_list, open_file)
# open_file.close()

open_file = open(file_name, "rb")
loaded_list = pickle.load(open_file)
open_file.close()

print(loaded_list)