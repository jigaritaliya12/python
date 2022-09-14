#for loop with list 
#findout whether given fruit name exist or not

fruits = ['apple','banana','mango','graps','pinapple','orange','kiwi']
print(fruits)
favourite = input("enter your favouite fruit name ") #mango
isFound = False #assume not found
position=1
for item in fruits:
    if favourite==item:
        print(f"your favorite fruit is in list at {position} ")
        isFound=True
        break
    position=position+1
if isFound==False:
    print("your favourite fruit not found in list")
    