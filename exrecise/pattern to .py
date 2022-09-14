#write a program to print following series (Lucas series)

# 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843
a=2
b=1
# number=0

# while number<=100:
#     n=ln-1+ln-2
#     print(n)

a=2
b=1
n=10
for i in range(1):
    c=i+1+i
print(c)
    
c=(i+1)+i
print(c)
a=c+b
print(a)
b=a+c
print(b)

