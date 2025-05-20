from collections import deque
from math import floor

expr = input().split()
operators = deque([])
result_mid = 0

mapper = {'*': lambda a, b: a * b,
          '/': lambda a, b: a // b,
          '+': lambda a, b: a + b,
          '-': lambda a, b: a - b
          }

for char in expr:
    if char not in mapper:
        operators.append(int(char))
    else:
        while len(operators) > 1:
            first = operators.popleft()
            second = operators.pop()
            operators.appendleft(mapper[char](first, second))

print(operators[0])