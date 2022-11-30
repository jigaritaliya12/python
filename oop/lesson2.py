#example instrance variable
class triangle:
    def setheight(self,h):
    #example instrance variable
        self.height=h
    def setbase(self,b):
    #example instrance variable
        self.base=b
    def getarea(self):
        area=0.50*self.base*self.height
        return area
    
#creat one object
t1=triangle()

b=int(input("enter your base"))
t1.setbase(b)

h=int(input("enter your height"))
t1.setheight(h)

area=t1.getarea()
print(area)
    
    
