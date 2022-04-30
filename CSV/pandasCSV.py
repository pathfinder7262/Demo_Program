#pandasCSV.py
import pandas as pd
rec=pd.read_csv("csvFile.csv")
print(rec)
print(rec.loc[5,"mrk"])
