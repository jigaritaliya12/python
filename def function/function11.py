#default argument values concept
def getintrest(amount,rate=10,year=1):
    intrest=(amount*rate*year)/100
    return intrest

a=int(input("enter your amount"))
r=int(input("enter your rate"))
y=int(input("enter your years"))

result=getintrest(a,r,y)
print(f"intrest is {result}")






