#read data from file and write data into file 
filereader=open('source.txt','r')
filewriter=open('destination.txt','w')
for line in filereader:
    print(line,end='')
    filewriter.write(line)
filereader.close()
filewriter.close()
