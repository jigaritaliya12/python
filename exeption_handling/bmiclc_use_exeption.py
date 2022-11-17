   # write a program to findout bmi of user using given weight and height with exceptional handling 
while 1==1:
 try:
  height=float(input("enter your height in cm"))
  weight=float(input("enter your weight in kg"))
  bmi=weight/(height/100)**2
  print(f"your bmi  is {bmi}")

  if bmi<=18.4:
    print("you are under weight")
  elif bmi<=24.9:
    print("you are healthy")
  elif bmi<=29.9:
    print("you are over weight")
  elif bmi<=34.9:
    print("you are severely over weight")
  elif bmi<=39.9:
    print("you are obese")
  else: 
    print("you are severely obese")
    break
 except ValueError:
    print("in valide input ")
    print("only digit are allowed")
print("good bye...")
    
