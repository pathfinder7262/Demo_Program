import re

textdata="Ramu  got  56 marks and whose mail id is ramu.ibm@ibm.com , Raju got 66 marks and whose mail id is raju.tcs@tcs.com , Pujitha got 99 marks and whose mail id is puji.wipro@wipro.com , Arien got 88 and whose mail id is arien.paypal@paypal.com , Bharath got 88 marks and whose mail id is bharath.google@google.com , Rasmi got 78 marks and whose mail id is raasmi123.ge@ge.net , Rossum got 77 marks and whose mail id is rossum4.psf@psf.org.net and Gosling got 44 and whose mail id is gosling.sun@sun.com and kvr got 11 marks and whose mail id is kvr.igatemnc@igate.com and Mayur got 99 and whose mail id is mayur2.igatemnc@igate.com and Gauravj got 69 and whose mail id is gaurav.apple@apple.com"

mails=re.findall("\S+@\S+",textdata)
print("-"*50)
print("All Student Mails Ids")
print("-"*50)
for mail in mails:
	print("\t{}".format(mail))
print("-"*50)
