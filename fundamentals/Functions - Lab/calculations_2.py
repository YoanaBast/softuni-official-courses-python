command = input()

def math_ops(a, b):
    if command == 'subtract':
        return a - b
    elif command == 'divide':
        return a // b
    elif command == 'add':
        return a + b
    elif command == 'multiply':
        return a * b

user_a = int(input())
user_b = int(input())

print(math_ops(user_a,user_b))