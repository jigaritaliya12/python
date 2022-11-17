#first example of exception handling mechanism

while 1==1:
 try:
    num1=int(input("enter your first number"))
    num2=int(input("enter your second number"))
    
    result=num1/num2
    print(result)
    break
    
 except ValueError:
    print("invalid number")
    print("only digit are allowed")
 except ZeroDivisionError:
    print("invalid number")
    print("zero not a valid vallue")
    
print("good bye...")