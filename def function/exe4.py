#write a program that has function that square and qube of given number (use multiple value return concept)
def sum(*values):
    total=0
    for item in values:
        total=total + item 
    return total

total = sum(10,20)
print(total)
total = sum(10,20,30,40)
print(total)
total = sum(10,20,30,40,50,60)
print(total)
