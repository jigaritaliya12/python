#write a program to findout factorial of given number
#input -> 5 -> 5 x 4 x 3 x 2 x 1 = 120
#input -> 6 -> 6 x 5 x 4 x 3 x 2 x 1 = 720

number=int(input("enter your number"))
multiplier = 1
answer=1
while multiplier<=number:
    answer = answer * multiplier 
    multiplier = multiplier + 1
    
print(f"factorial is {answer} of {number}")