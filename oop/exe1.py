'''create class SimpleInterest that has following methods 
  setAmount(amt)
  setRate(rat)
  setYear(yr)
  getInterest() which return simple Interest'''
  
  
class intrest:
    def setamount(self,a):
        self.amount=a
    def setrate(self,r):
        self.rate=r
    def setyear(self,y):
        self.year=y
    def getresult(self):
        result=self.amount*self.rate*self.year/100
        return result
    
#creat one object
i1=intrest()

a=int(input("enter your amount"))
i1.setamount(a)

r=int(input("enter your rate"))  
i1.setrate(r)    

y=int(input("enter your year"))
i1.setyear(y)

result=i1.getresult()
print(result)
