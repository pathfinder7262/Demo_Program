#create new folder in current working directory
#mkdir.py
import os
try:
    cwdnm=os.mkdir("G:\CDricwBackUP\cccc\yy\yy")
except FileExistsError:
    print("file already exist")
except FileNotFoundError:
     print("file not found")
    
