#remove folder
#rmdir.py

import os

try:
    os.rmdir("cc")
    os.rmdir("G:\india\Mahars\jalgaon\khote nagar")
    print("removed")
except FileNotFoundError:
    print("folder not found")
