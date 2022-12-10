class programmar:
    company="microsoft"
    
    #constructor
    def __init__(self,name,product):
     self.name=name
     self.product=product
        
    def getinfo(self):
        print(f'the name of the {self.company} programmar is {self.name} and the product is {self.product}')
        
jigar=programmar("jigar","whatsapp")
parth=programmar("parth","instagram")

jigar.getinfo()
parth.getinfo()