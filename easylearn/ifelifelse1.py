# write a program to develope basic mathematical calculator that perform following operations 
# addition, substraction, multiplication, division 

num1=int(input("enter your frist number"))
num2=int(input("enter your second number"))

print("press 1 for addition")
print("press 2 for substaction")
print("press 3 for multiplication")
print("press 4 for devision")

choice=int(input("enter your choice"))
result=None
if choice==1:
    print("it is addition")
    result=num1+num2
elif choice==2:
    print("it is substraction")
    result=num1-num2
elif choice==3:
    print("it is multiplication")
    result=num1*num2
elif choice==4:
    print("it is decision")
    result=num1/num2
else:
    print("not valid choice")
if result!=None:
    print("result is ",result)
        
