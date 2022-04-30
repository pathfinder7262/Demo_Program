#46.wapp which  will read the emp records from the file and display on the console.
#46.emp_pkl_read_data.py
import pickle

try:
    with open("emppkl.txt","rb") as empr:
        while(True):
            try:
                obj =pickle.load(empr)
                for i in obj:
                    print(i)
except EOFError:
    print("+++")
except:
    print("File not found")
