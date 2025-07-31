#Import Built-in Array Module and Display Namespace
import array
for name in array.__dict__:
    print(name)