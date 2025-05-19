from collections import deque
from math import floor

expr = input().split()
operators = deque([])
result_mid = 0

for char in expr:
    if char == '*':
        result_mid = operators.popleft()
        for digi in operators:
            result_mid *= digi

        operators = deque([])
        operators.append(result_mid)
        result_mid = 0
        continue

    elif char == '/':
        result_mid = operators.popleft()
        for digi in operators:
            result_mid = floor(result_mid / digi)

        operators = deque([])
        operators.append(result_mid)
        result_mid = 0
        continue

    elif char == '+':
        result_mid = operators.popleft()
        for digi in operators:
            result_mid += digi

        operators = deque([])
        operators.append(result_mid)
        result_mid = 0
        continue

    elif char == '-':
        result_mid = operators.popleft()
        for digi in operators:
            result_mid -= digi

        operators = deque([])
        operators.append(result_mid)
        result_mid = 0
        continue

    operators.append(int(char))

print(operators[0])