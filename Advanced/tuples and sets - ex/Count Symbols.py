expr = input()
ex_set = set()

for char in expr:
    ex_set.add(char)

order = sorted(ex_set)
for chr in order:
    c = expr.count(chr)
    print(f'{chr}: {c} time/s')
