n = int(input())
stack = []
#mapper:
functions = {
    '1': lambda x: stack.append(int(x)),
    '2': lambda: stack.pop() if stack else None,
    '3': lambda: print(max(stack)) if stack else None,
    '4': lambda: print(min(stack)) if stack else None,
}

for _ in range(n):
    command = input().split()
    functions[command[0]](*command[1:])

stack.reverse()
print(', '.join(map(str, stack)))