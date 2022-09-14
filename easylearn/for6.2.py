#write a program to count vowels in given string (aeiou)
name = input("entr name")
count=0 
vowels = ['a','e','i','o','u','A','E','I','O','U']
for letter in name:
    if letter in vowels:
        count=count+1 
print(count)