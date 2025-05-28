from functools import reduce

def operate(op, *args):

    if op =='+':
        return reduce(lambda x, y: x + y, args)
    elif op =='-':
        return reduce(lambda x, y: x - y, args)
    elif op =='*':
        return reduce(lambda x, y: x * y, args)
    elif op =='/':
        return reduce(lambda x, y: x / y, args)

print(operate("+", 1, 2, 3))