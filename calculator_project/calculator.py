def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error"
    return a / b

def power(base, exp):
    return base ** exp

def sqrt(a):
    if a < 0:
        return "Error"
    return a ** 0.5