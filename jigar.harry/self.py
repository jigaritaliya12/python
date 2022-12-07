class Employee:
    company="google"
    def getsalary(self):
        print(f"salary for this employee working in {self.company} is {self.salary}")
harry=Employee()
harry.salary=100000
harry.getsalary()