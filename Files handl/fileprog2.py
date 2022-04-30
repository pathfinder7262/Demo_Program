#fileprog2.py
#prog for file opening modes

ketanp= open("file1")
id(ketanp)
print("file opened succesfully ")

print("="*50)
print("file opened succesfully")
print("="*50)
print("Type of ketanp={}".format(ketanp))   #TextIOWrapper--node
print("Mode of  ketanp={}".format(ketanp.mode)) 
print("is the file readable?={}".format(ketanp.readable()))    #==>true
print("is the file readable?={}".format(ketanp.writable()))    #==>false
print("is the file closed?={}".format(ketanp.closed))
print("="*50)
    
#mode==>closed   readable    writable
