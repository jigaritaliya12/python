'''write a program to findout compound interest of given amount,rate and year using range for loop '''

amount=int(input("enter your amount"))
rate=int(input("enter your rate"))
year=int(input("enter your year"))

a=amount*(1+(rate/100))**year
ci=a-amount
print(ci)

