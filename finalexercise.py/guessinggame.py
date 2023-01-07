import random
n=random.randrange(1,10)
guess=int(input("enter your number"))

while n!= guess:
    if guess<n:
        print("your number is  low")
        guess=int(input('enter your number again'))
    elif guess>n:
        print('your number is high')
        guess=int(input("enter your number again"))
        
    else:
        break
print("you are win")