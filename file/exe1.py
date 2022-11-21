  #write a program to accept file name from user. if file exists ask user whether to write content into it or add new content into it 
  
filename=input("enter your file name")
mode="w"
file=open(filename,mode)
if filename in filename:
  print('enter your number')
  filecontant=input("write some text to be  written into file")
  file.write(filecontant)


else:
  print('nota enter your number')
file.close



