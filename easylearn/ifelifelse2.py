# write a program to findout whether shape is landscape or potrait or square from given length and width

length=int(input("enter length"))
width=int(input("enter width"))

if length==width:
    print("this is square")
    
elif length>width:
    print("this is landscape")
else: 
    print("this is potrait")
    
print("good bye...")
    
