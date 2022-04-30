#con_package
import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",passwd="",database="kvr")
#cur = con.cursor()
def dcon():
    return con

