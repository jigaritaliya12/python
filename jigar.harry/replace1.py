with open("sample.txt")as f:
    contant=f.read()
contant=contant.replace("jigar","parth")
with open('sample.txt','w') as f:
    f.write(contant)