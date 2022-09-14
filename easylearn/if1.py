# write a progrram to findout qube of given positive number

number=int(input("enter number"))
if number<0:
    print("number is nagtive number so enter please positive number")
    number=0-number
qube=number*number*number
print(f"qube of {number}={qube}")