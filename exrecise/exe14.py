''' Write a Python program to calculate income tax, gross income, net income from monthly income given by user 

yearly income     tax rate
<3,00,000         5%  

>=3,00,000
<5,00,000         10%  

>=5,00,000
<8,00,000         20%

>=8,00,000        30%  '''

monthlyincome=int(input("enter your monthly gross income"))
grossincome=monthlyincome*12
print("yerly income")
print(grossincome)
print("income tax")
if monthlyincome<=300000:
    tax=grossincome*5/100
    print(tax)
    netincome=grossincome-tax
    print("net income")
    print(netincome)
   
elif monthlyincome>=300000 and monthlyincome<=500000:
    tax=monthlyincome*10/100
    print(tax)
    netincome=grossincome-tax
    print("net income")
    print(netincome)
elif monthlyincome>=500000 and monthlyincome<=800000:
    tax=monthlyincome*20/100
    print(tax)
    netincome=grossincome-tax
    print("net income")
    print(netincome)
elif monthlyincome>=800000:
    tax=monthlyincome*30/100
    print(tax)
    netincome=grossincome-tax
    print("net icome")
    print(netincome)
    
print("good bye.......")



