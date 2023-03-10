'''  Super keyword in Python
The super() keyword in Python is used to refer to the parent class. It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes.

When a class inherits from a parent class, it can override or extend the methods defined in the parent class. However, sometimes you might want to use the parent class method in the child class. This is where the super() keyword comes in handy.

Here's an example of how to use the super() keyword in a simple inheritance scenario:  
    '''
'''class Employee: 
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    super().__init__( name, id)
    self.lang = lang

rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "2345", "Python")
print(harry.name)
print(harry.id)
print(harry.lang)

'''

class worker:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class kamdar(worker):
    def __init__(self,name,id,lang):
     super().__init__(name,id)
     self.lang=lang
    
jigar=worker("rahul das",'220')
harshil=kamdar("yash",'330','english')
print(harshil.name)
print(harshil.id)
print(harshil.lang)









     
