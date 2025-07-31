#validate integer input with raise valuerro
def get_number(val):
    try:
        value = int(input(val))
        return value
    except ValueError:
        print("Error : Invalid input, input a valid intput")
        
a=get_number("input an integer: " )
print("Input value :", a)