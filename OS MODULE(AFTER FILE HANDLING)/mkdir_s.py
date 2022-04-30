#create root folder,sub folder,sub-sub folder in current working directory
#mkdir_s.py
import os
try:
    cwdnm=os.makedirs("G:\india\Mahars\jalgaon\khote nagar\cc\cc\cc\cc\cc")
    print("cc")
except FileExistsError:
    print("file already exist")
except FileNotFoundError:
     print("file not found")
    
