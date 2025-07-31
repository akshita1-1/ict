#sum of all the numbers in list
def findsum():
    sum=0
    l=[1,2,3,4]
    for i in range(0,4):
        sum=sum+l[i]
    return(sum)
print(findsum())