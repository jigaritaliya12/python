# Write a Python program to calculate final electricity bill based upon below given criteria. take monthly electricity unit from user as input. 

#units           price  per unit 
#<100             1
#>=100 & <200     2 
#>=200 & <300     3
#>=300 & <400     4
#>=400            5

#also calculate 5% percentage energy charge on total bill amount & display total amount 

unit=int(input("enter your electricity unit"))
if (unit<100):
    amount=unit*1
    print(amount)
elif(unit>=100 and unit<200):
    amount=unit*2
    print(amount)
elif(unit>=200 and unit<300):
    amount=unit*3
    print(amount)
elif(unit>=300 and unit<400):
    amount=unit*4
    print(amount)
elif(unit>=400):
    amount=unit*5
    print(amount)
    
answer=amount*5/100
print(answer)
    

