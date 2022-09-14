''' write a program to copy list in reverse fashion into another list but duplicate value must be skiped from list. 
list = ['mango','orange','pinapple','graps','custerd-apple','orange','pinapple']
reversedlist = ['pinapple', 'orange', 'custerd-apple', 'graps', 'mango']'''

fruits=['mango','orange','pinappale','graps','custerd-apple','orange','pinappale'] 
fruits2=[]
ok=[]
for item in reversed(fruits):
    ok.append(item)
for i in ok:
    if i not in fruits2:
        fruits2.append(i)
    else:
        print(i)
print(fruits2)

