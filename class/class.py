'''def funct(**a):
    print(type(a))
    pass

funct(e=1,b=2,c=3,d=4)
'''
#anonmyous function na call krre h na he define krre h seedhe variable and parameters krre h print
'''add = lambda a,b : a+b
print(add(6,1))'''

#higher order function
#in GENERATOR we use yield to provide output one at a time(reference oriented after one execution it pauses and stores the state and whenn called resumes from the previous state)  
#DECORATAR is a function that enhances the functionality of different function
#@func_B
#func_A : simple function 
 #   a+b
#func_B : Decorator 
 #    func_A + c
 
 #OOPs

 #OOPs :is used to represent logical and physical entity
 '''magicmethod , dundar are replacement of constructor 
 magic method- __init__ , self , values'''
 #class mouse:it is the blueprint of class(represent any kind of mouse)
 '''syntax of class : "class classname"'''
 #object : type of mouse , model of mouse 
 '''syntax of object(function calling) :obj = classname("value1" , '"value2") '''
 '''inheritance , polymorphism , encapsulation, abstraction are FEATURES OF CLASS''' 
 '''by default we just have constructor setter and getter which are not pre defined'''
 #1. ABSTRACTION: hiding complex implementation and showing only neccessary functionality
 #2. ENCAPSULAION:creation of class
 #3. INHERITANCE: derived class that is child class can access the functionality or features of the parent class
 #4. POLYMORPHISM: multi function have same name but different agruments and type of argument
 
 '''EXAMPLE '''
class class1:
    def__init__(self): #(push nhi krege obj automatically aajayega)
        pass
    id=10
    name='aditya'
    
#obj = class1() #object creation

class = class2(class1):
    add= 'qwerty'
    
obj = class2()

print(obj.name)


#def func
'''def func(self):
    pass
def func(self,a):
    self.a=a
namespace conflicting hoga'''


#GENERATOR
'''uses yield to give output one at a time''' 
