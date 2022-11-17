    #write a program to findout factorial of given number exceptional handling 
while 2==2:
 try:
  num=int(input("enter your number"))
  factorial=1
  if num<0:
    print("sorry factorial  does not  exist for nagative number")
  elif num==0:
     print("the factorial  of 0 is 1")
  else:
    for i in range(1,num+1):
            factorial=factorial*i
    print("factorial is ",num,"is",factorial)
    break
 except ValueError:
    print("in valide input only valid for integer vallue")
    
