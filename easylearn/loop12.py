#write a program to print given range in reverse order
# start = 10
# stop = 51
# 50 50 49 48 47 .... 10

start=int(input("enter your fristnumber"))
stop=int(input("enter your second number"))
for number in range(stop,start,-1):
    print(number,end=' ')