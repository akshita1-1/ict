#person age with age calculation
class person:
    def __init__(self,name,country,yob):
        self.name = name
        self.country = country
        self.yob = yob 
     
    def findage(self):
        return 2025 - self.yob
    
obj = person("Arti Dhavre" , "India", 1974)
print(obj.findage())