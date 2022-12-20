class employee:
    company='camel'
    salary=100
    location='delhi'
    @classmethod
    def changesalary(cls,sal):
        cls.salary=sal 
    
e =employee()   
print(e.salary)
e.changesalary(200)
print(e.salary)
print(employee.salary)
