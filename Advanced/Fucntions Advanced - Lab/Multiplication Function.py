def multiply(*args):
    sumi = 1
    for item in args:
        sumi *= item
    return sumi

print(multiply(1, 4, 5))