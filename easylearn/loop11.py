#write a program to findout & print odd number between given range 
# start = 10
# stop = 51
# 11,13,15,17 .... 49
start = int(input("enter first number"))
stop = int(input("enter second number"))
for number in range(start,stop):
    if number%2==1:
        print(number,end=' ')