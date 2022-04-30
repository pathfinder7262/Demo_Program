import  cx_Oracle
try:
	kvrcon=cx_Oracle.connect("system/orcl@127.0.0.1/orcl")
	print("\ntype of kvrcon={}".format(kvrcon))
	crobj=kvrcon.cursor()
	print("\ntype of crobj={}".format(crobj))
	print("\nConnection obtained successfully!")
except cx_Oracle.DatabaseError as db:
	print("Coonection Denied due wrong details")
	

