#find simple intrest for using exeption method
try:
 a=int(input("enter your amount"))
 b=int(input("enter your rate"))
 c=int(input("enter your year"))

 result=a*b*c/100
 print(result)

except ValueError:
    print("invalid amount ")
    print("only digit are allowed")
    
