class worker():
    def _init_(self, name, payment):
        self.name = name
        self.payment = payment
    def lastName(self):
        name= self.name
        name.split()[-1]
        return name
    def giveRaise(self, percent):
        self.payment *= (1.0 + percent)
        
b=(input("enter lastname"))
c=int(input("enter giveraise"))


a=worker()


a.lastName()

a.giveRaise()