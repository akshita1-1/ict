#Random Number Generator 
import random
def __Randomno__(end):
    yield random.randint(1,end)
    
end = int(input("Input the End value :"))

for i in __Randomno__(end+1):
    print(i)