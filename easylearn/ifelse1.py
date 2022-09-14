#write a program to findout whether person is eligible for voting & driving licence or not from  user given age
# if person age is above 17 then person is eligible for voting & licence
# if person age is less then 18 then person is not eligible for voting & licence

age=float(input("enter your age"))
if age>=18:
    print("you are eligible for licence")
else:
    print("you are not eligible for licence")
    
print("good bye....")