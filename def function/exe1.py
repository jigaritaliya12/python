'''write a program that has function that return volume of room from given length,width,height in which length and height are optional. (use default arguments values)'''


def getvolume(width,lenth=30,height=20):
    volume=width*lenth*height
    return volume

a=int(input("enter your width"))
b=int(input("enter your lenth"))
c=int(input("enter your height"))

result=getvolume(a,b,c)
print(f"volume is {result}")
