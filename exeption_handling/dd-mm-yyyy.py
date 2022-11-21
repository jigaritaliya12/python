    #write a program to convert dd-mm-YYYY date into YYYY-mm-dd format with exceptional handling mechanism 
    
import datetime

day=int(input("enter your day"))
month=int(input("enter your month"))
year=int(input("enter your year"))

date=datetime.date(year,month,day)
print(date)


