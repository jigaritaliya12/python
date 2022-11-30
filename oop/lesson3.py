class box:
    #constructor
    def __init__(self,lenght,width,deapth):
        #creat instance variable
        self.length=lenght
        self.width=width
        self.deapth=deapth
    def getarea(self):
        #crating local variable area 
        area=self.length*self.width
        return area
    def getvolume(self):
        volume=self.length*self.width*self.deapth
        return volume
length=int(input("enter your length"))
width=int(input("enter your width"))
deapth=int(input("enter your deapth"))

#creating object
#objectname=class()

b1=box(length,width,deapth)

area=b1.getarea()
print(area)

volume=b1.getvolume()
print(volume)