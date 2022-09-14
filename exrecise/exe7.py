# write a program to findout power of given base and exponent. if base or exponent is negative number then convert it into positive number 
import math
a=int(input("enter base"))
b=int(input("enter exponent"))

if a>0:
    print("it is positive")
    number1=a
else:
    number1=a-0
if b>0:
    print("it is positive")
    number2=b
else:
    number2=b-0
power=pow(number1,number2)
print(power)
 


