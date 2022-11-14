import random

def getotp(length):
    list=['1','2','3','4','5','6','7','8','9','0']
    random.shuffle(list)
    size=len(list)-1
    count=1
    password=''
    while count<=length:
         position = random.randint(0,size)
         password = password + list[position]
         count=count+1
    return password
        