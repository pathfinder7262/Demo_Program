#pickle2
import pickle
try:
    with open("stud.data","rb") as rp:
        print("="*50)
        print("Student detail")
        print("="*50)
        while(True):
            try:
                obj = pickle.load(rp)
                for val in obj:
                    print(val)
              
            except EOFError:
                print("---------------------------------------------------------------------------------------")
            break
except FilrNotFoundError:
    print("file is not there")
