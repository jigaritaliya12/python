class Employee:
    company='google'
    
harry=Employee()
rajni=Employee()
print(harry.company)
print(rajni.company)
Employee.company='utube'
print(harry.company)
print(rajni.company)