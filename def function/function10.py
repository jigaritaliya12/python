#with return value with argument function 


def getsquare(number):
    squar=number*number
    return squar
number=int(input("enter your number"))
squar=getsquare(number)
print("squaris",squar)

def getqube(number):
    qube=number*number*number
    return qube
number=int(input("enter your number"))
qube=getqube(number)
print("qube is",qube)

def getaddition(number):
    addition=number+number
    return addition
number=int(input("enter your number"))
addition=getaddition(number)
print("addition",addition)

    