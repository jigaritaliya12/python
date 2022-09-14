#write a program that has function which will print name of given day of week 
#printDayName(day)


def getday(number):
    if number==1:
        print("monday")
    elif number==2:
        print("tuesday")
    elif number==3:
        print("wednesday")
    elif number==4:
        print("thursday")
    elif number==5:
        print("friday")
    elif number==6:
        print("saturday")
    elif number==7:
        print("sunday")
    else:
        print("please enter your right number")
         
number=int(input("enter day of week"))
getday(number)


    