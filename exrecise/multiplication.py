#write a program to print reverse multiplication table of given number using range for loop

num=int(input("Enter the number"))
for i in range (10,0,-1):
  print(f"{num}*{i}={num*i}")
  