#remove folder hierarchy
#movedirs.py

import os

try:
    os.removedirs("G:\india\Mahars\jalgaon\khote nagar")
    print("removed")
except FileNotFoundError:
    print("folder not found")
except OSError:
    print("Folder not Empty")
    
