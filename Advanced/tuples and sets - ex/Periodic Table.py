n = int(input())
table = set()

for _ in range(n):
    command = input().split()
    for x in command:
        table.add(x)

for chem in table:
    print(chem)