# write a program to accept month number from user. display message "this month has 28 or 29 days" if month if february. if month is january,march,may etc then display message "this month has 31 days" otherwise print message "this month has 30 days"

month=input("enter your month")
print(f"enter your month{month}")
if month=='february':
    print("28 days this month")
else:
    if month=='january'or month=='march'or month=='may'or month=='july'or month=='august'or month=='octomber'or month=='december': 
        print("31 days of this month")
    else:
        print("30 days this month")
    print("good bye....")