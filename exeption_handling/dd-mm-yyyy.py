    #write a program to convert dd-mm-YYYY date into YYYY-mm-dd format with exceptional handling mechanism 
    
import datetime
current_day=datetime.date.today()
print(current_day)

convertformate=datetime.date.strftime(current_day,"%y/%m/%d")
print(convertformate)


