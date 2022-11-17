#write a program to findout total & average of all integer value in list 

number=[12,'jigar',22,False]
total=0
count=0
for item in number:
    print(item)
    try:
        if item==False or item==True:
            print(f"{item} item is a boolean vallue so it is skiped")
        else:
         total=total+item
         count=count+1 
         
    except TypeError:
        print(f"{item} is not a number so it is skiped ")   
print(count)  

try:
   avrage=total/count 
   print(total)
   print(avrage)
   
except ZeroDivisionError:
 print("ether list is empty value or all value are invalide")


    