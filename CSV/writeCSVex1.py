#writeCSVex1.py
import csv
rec = [[20,"cc",78],[30,"pk",69],[40,"ps",50]]
with open("pyCSV.csv","a") as wp:
    csvw=csv.writer(wp)
    csvw.writerow(rec)
    print("\nDataWritten to the csv file")
