'''class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showdetailes(self):
        print(f"the name of employee:{self.id} is {self.name}")
class microsoft(employee):
    def showcompany(self):
      print("the default company is microsoft")
        
e1=employee("jigar italiya",200)
e1.showdetailes()
e2=microsoft("jigar",400)
e2.showcompany()'''


class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id 

  def showDetails(self):
    print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
  def showLanguage(self):
    print("The default langauge is Python")


e1 = Employee("Rohan Das", 400)
e1.showDetails()
e2 = Programmer("Harry", 4100)
e2.showDetails()
e2.showLanguage()