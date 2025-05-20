from collections import deque

def present(x: int):
    res = ''
    if x == 150:
        res = 'Doll'
    elif x == 250:
        res = 'Wooden train'
    elif x == 300:
        res = 'Teddy bear'
    elif x == 400:
        res = 'Bicycle'
    else:
        res = 0

    return res

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

toys = {}


while materials and magic:
    if magic[0] == 0 and materials[-1] == 0:
        magic.popleft()
        materials.pop()
        continue

    if magic[0] == 0:
        magic.popleft()
        continue

    if materials[-1] == 0:
        materials.pop()
        continue

    score = magic[0] * materials[-1]
    if score < 0:
        materials.append(magic.popleft() + materials.pop())

    elif score > 0:
        product = present(score)
        if product == 0: #potential bug i dont know how none works. may change for 0 # yeah
            magic.popleft()
            materials[-1] += 15

        else:
            if product not in toys:
                toys[product] = 1
                magic.popleft()
                materials.pop()
            else:
                toys[product] += 1
                magic.popleft()
                materials.pop()


task = {1: ['Doll', 'Train'],
        2: ['Teddy bear', 'Bicycle']}

# if task[1] in toys or task[2] in toys: # potential bug here
toys_s = dict(sorted(toys.items()))
if all(toy in toys_s for toy in task[1]) or all(toy in toys_s for toy in task[2]):
    print("The presents are crafted! Merry Christmas!")

else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, materials[::-1]))}")

if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

if toys:
    for key, value in toys_s.items():
        print(f'{key}: {value}')