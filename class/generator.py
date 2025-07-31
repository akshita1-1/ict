def ago(a):
    i=0
    while i<=a:
        yield i
        i+=1
for i in ago(5):
    print(i)



'''yield genrates a temporary memory and storage space unordered 
Use of Generator

'''


    