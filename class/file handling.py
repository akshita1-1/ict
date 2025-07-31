#file handling 
#var = open('<filename_ext>' , 'am')

#var.close()

#with open('<filename_ext>', 'am') as var #iss m close wala nhi chahiye sab ek line m ho jayega


with open ("myfile.txt" , "w") as file:
    file.write("hello")
with open("myfile.txt", "r") as file:
    content=file.readlines()
    print(type(content))