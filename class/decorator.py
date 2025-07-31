#decorator 
def log_detect(func):
    def wrapper(a,b):
        print("Function name:", func.__name__)
        print("Arguments passed:",a,b)
        result = func(a,b)
        print("Returned:",result)
        return result
    return wrapper

@log_detect
def add(x,y):
    return x+y

add(4,6)