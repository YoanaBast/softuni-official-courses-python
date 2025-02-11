names = input().split(", ")
sorted = sorted(names, key=lambda x: (-len(x), x))
print(sorted)