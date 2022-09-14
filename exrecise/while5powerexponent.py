#write a program to findout power of given base and exponent using loop  

a=int(input("enter your base"))
b=int(input("enter your exponent"))
    
base = a
exponent = b

result = 1

while exponent != 0:
    result *= base
    exponent-=1
print(result)
 