'''write a program that has function that return area of triangle from given base and height in which  height is optional. (use default arguments values)'''

def getarea(base,height):
    area =1/2 (base * height)
    return area

a=int(input("enter your base"))
b=int(input("enter your height"))

result=getarea(a,b)
print(result)

