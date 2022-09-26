#multiple value return
def getScienceMarit(maths,science,english,gujarati,hindi,sanskrut):
    print(f"maths = {maths} science = {science} english = {english} gujarati = {gujarati} hindi = {hindi} sanskrut = {sanskrut}")
    total = maths + science
    average = total/2 
    return total,average

average = getScienceMarit(60,70,80,90,95,99)
print(average)