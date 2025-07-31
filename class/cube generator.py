#cube generator
def __Cubes__(n):
    for i in range(1, 1+n):
        yield i**3


n = int(input("enter a number :"))

    
for i in __Cubes__(n):
    print(i)