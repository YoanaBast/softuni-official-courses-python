n, m = input().split()
nset = set()
mset = set()

for _ in range(int(n)):
    nset.add(input())

for _ in range(int(m)):
    mset.add(input())

unique_intersection = nset & mset
for x in unique_intersection:
    print(x)