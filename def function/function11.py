#default argument values concept
def getintrest(amount,rate=10,year=1):
    intrest=(amount*rate*year)/100
    return intrest

amount=int(input("enter your amount"))
rate=int(input("enter your rate"))
year=int(input("enter your years"))

result=getintrest(amount,rate,year)
print(f"intrest is {result}")






