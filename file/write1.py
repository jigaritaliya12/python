#write a program to create file in python and write content into file 
filename=input("enter your file name ")
mode='w'
try:
    
 file=open(filename,mode)
 filecontant=input("write some text to be  written into file")
 file.write(filecontant)
 file.close
 print("file creat")
except FileNotFoundError:
    print("no such directory exist given in file name")
except PermissionError:
    print("you dont have permission to create file at this location")