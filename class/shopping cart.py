#shopping cart class
class ShoppingCart:    
    def __init__(self,items):
        self.items = items
    
    def addItems(self,name):
        self.items.append(name)
        
obj = ShoppingCart([])
obj.addItems("apple")
obj.addItems("orange")
obj.addItems("lotion")
obj.addItems("bodywash")
obj.addItems("pineapple")
obj.addItems("papaya")
print(obj.items)
