# How to create an empty class in Python?

''' answer   empty class is a class that does not have any code defined within its block. It can be created using the pass keyword. However, you can create objects of this class outside the class itself. IN PYTHON THE PASS command does nothing when its executed. it’s a null statement. '''

# example

class a:
  pass
obj=a()
obj.name="xyz"
print("Name = ",obj.name)