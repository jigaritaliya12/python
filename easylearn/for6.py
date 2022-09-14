#write a program to count vowels in given string (aeiou)
name = input("enter name")
count=0
for letter in name:
    if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u' or letter=='A' or letter=='E' or letter=='I' or letter=='O' or letter=='U':
        count=count+1 
print(count)
