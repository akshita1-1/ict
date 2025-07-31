#divide numbers 
def divide_num(a,b):
    try:
        result = a/b
        print("Result :",result)
    except ZeroDivisionError:
        print("The divison by zero oeration is not allowed.")
        
numerator = 7000
denominator= 35
divide_num(numerator,denominator)
        