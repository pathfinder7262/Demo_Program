#readCSV.py

import csv
with open("csvFile.csv","r") as csvrp:
    rec=csv.reader()
    for i in rec:
        print(i)
    
