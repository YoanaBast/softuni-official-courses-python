# Create a function that receives three parameters, calculates a result depending on the given operator,
# and returns it. Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers.
# The operator can be one of the following: "multiply", "divide", "add", and "subtract".

def subtracting(a, b):
    return a - b

def dividing(a, b):
    return a // b

def adding(a, b):
    return a + b

def multiplying(a, b):
    return a * b
command = input()
user_a = int(input())
user_b = int(input())


if command == 'subtract':
    print(subtracting(user_a,user_b))

elif command == 'divide':
    print(dividing(user_a,user_b))

elif command == 'add':
    print(adding(user_a, user_b))

elif command == 'multiply':
    print(multiplying(user_a, user_b))