#write a program to findout whether given number is prime number or not 
number=int(input("enter your number"))

reminder = 0
divider = 2

while divider<number:
    reminder = number % divider #1
    if reminder==0:
        print("it is not prime number")
        break
    else:
        divider=divider+1 #3
    
if divider==number:
    print("it is prime number")
