opening_stack = []
expr = list(input())

for index in range(len(expr)):
    if expr[index] == '(':
        opening_stack.append(index)
    elif expr[index] == ')':
        start = opening_stack.pop()
        print(''.join(expr[start:index+1]))

