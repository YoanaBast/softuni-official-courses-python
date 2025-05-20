from collections import deque

def honey_make(bee, proc, nec):
    result = 0
    if proc == '+':
        result = bee + nec
    elif proc == '-':
        result = bee - nec
    elif proc == '*':
        result = bee * nec
    elif proc == '/':
        result = bee / nec

    return abs(result)

honey = 0

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
process = deque([x for x in input().split()])

while bees and nectar:
    if process[0] == '/' and nectar[-1] == 0:
        process.popleft()
        bees.popleft()
        nectar.pop()
        continue

    if nectar[-1] < bees[0]:
        nectar.pop()

    elif nectar[-1] >= bees[0]:
        pro = process[0]
        honey += honey_make(bees[0], pro, nectar[-1])
        process.popleft()
        bees.popleft()
        nectar.pop()

print(f"Total honey made: {honey}")

bee_str = map(str, bees)
nec_str = map(str, nectar)

if bees:
    print(f"Bees left: {', '.join(bee_str)}")
if nectar:
    print(f"Nectar left: {', '.join(nec_str)}")