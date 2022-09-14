"""write a program to count odd & even values in list 
numbers = [1,55,45,78,100]
odd values = 3
even values = 2"""
number=[1,55,24,78,100,111,12,13,14,15,42]

even_count = 0
odd_count = 0

for num in number:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)