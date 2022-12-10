class person:
    country="india"
    
    def __init__(self):
        print("initialization person....\n")
        
    def takebreth(self):
        print("i am breathing ....")

class Employee(person):
    company="honda"
    
    def __init__(self):
        super().__init__()
        print("initialization employee....\n")
        
    def getsalary(self):
        print(f"salary is {self.salary}")
        
    def takebreath(self):
        super().takebreth()
        print("i am an employee so i am lukily breathing...")

class programmer(Employee):
    company="fiverr"
    def __init__(self):
        print("initialization programmar....\n")
    def getsalary(self):
        print(f'no salary to progarammar so i am breathing++...')
        
# p = Person()
# p.takeBreath() 

# e = Employee()
# e.takeBreath() 

pr=programmer()
# pr.takeBreath() 

    
        
        
