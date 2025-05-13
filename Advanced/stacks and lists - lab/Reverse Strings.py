stack = list(input())
result = []
for i in range(len(stack)):
    result.append(stack.pop())
print(''.join(result))