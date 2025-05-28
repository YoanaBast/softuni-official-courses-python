from functools import reduce

def add(*args):
    return reduce(lambda x, y: x + y, args)

def subtract(*args):
    return reduce(lambda x, y: x - y, args)

def multiply(*args):
    return reduce(lambda x, y: x * y, args)

def divide(*args):
    return reduce(lambda x, y: x / y, args)

mapper ={
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def operate(op, *args):
    return mapper[op](*args)


print(operate("+", 1, 2, 3))