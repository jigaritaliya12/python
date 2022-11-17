#write a program to findout largest number from 3 given number using nested decision making 

num1=int(input("enter your fist number"))
num2=int(input("enter your second number"))
num3=int(input("enter your third number"))

print(f"num1={num1} num2={num2} num3={num3}")

if num1>num2:
    if num1>num3:
        print("num 1 is largest number")
    else:
        print("num 3 is largest number")
else:
    if num2>num3:
        print("num 2 is largest number")
    else:
        print("num 3 is largest number")
        
print("good bye....")
    
        

