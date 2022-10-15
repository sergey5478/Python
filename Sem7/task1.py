from re import A, X


x = 0
y = 0

def Number(a, b):
    global x
    global y
    x = a
    y = b

def Sum():
    return x + y 
