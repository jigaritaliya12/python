# write a program findout largest rectangle from two given rectangle length & width. 

lenth1=int(input("enter frist rectangle lenth"))
width1=int(input("enter frist rectangle width"))
if lenth1<width1:
    print(" it is a rectangle")
else:
    print("it is not rectangle please enter right lenth or width")
area1=lenth1*width1
print("it is frist rectangle area")
print(area1)

lenth2=int(input("enter second rectangle lenth"))
width2=int(input("enter second rectangle width"))
if lenth2<width2:
    print("it is a rectangle")
else:
    print("it is not a rectangle please enter right lenth or width")
area2=lenth2*width2
print("it is second rectangle area")
print(area2)

if area1>area2:
    print("rectangle 1 is big")
else:
    print("rectangle 2 is big")
print("good bye...")
