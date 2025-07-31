#function lambda generator
def compute(n):
    return lambda y:y * n
result = compute(6)
print("hexatuple the number of 40", result(40))
