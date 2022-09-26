#keyword argument concepts
def getScienceMarit(maths,science,english,gujarati,hindi,sanskrut):
    print(f"maths{maths} science{science} english{english} gujrati{gujarati} hindi{hindi} sanskrut{sanskrut} ")
    total=maths+science
    average = total/2
    return average
average = getScienceMarit(70,50,50,30,90,40)
print(f"average = {average}")