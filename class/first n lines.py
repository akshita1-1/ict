# first n lines
a=int(input("enter"))
with open("file.txt","w") as file:
    file.write("hello\nhellooo\nhello\nhelllooo")
    
with open("myfile.txt","r") as file:
    lines=file.readlines()
    for i in range(a):
        print(lines[i])
        

