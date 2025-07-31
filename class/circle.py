class circle:
    def __init__(self,radius):
        self.radius=radius
    def circlearea(self):
        return 3.14*self.radius*self.radius
    def circleperimeter(self):
        return 2*3.14*self.radius
obj = circle(20) 
print(obj.circlearea())
print(obj.circleperimeter())       
