import os

files=os.listdir('cluteredfolder')
i=1
for file in files:
 if file.endswith(".png"):
    print(file)
    os.rename(f"cluteredfolder/{file}",f'cluteredfolder/{i}.png')
    i=i+1