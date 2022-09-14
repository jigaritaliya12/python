#write a program to print following pattern 
# 10 20 40 80 160 320 ..... 10000

number=5

while number<=10000:
    answer=number+number
    print(answer)
    number=number+number