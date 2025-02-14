quantity_of_decor = int(input())
days_left = int(input())

spirit = 0
cost = 0

for day in range(1, days_left+1):

    if day % 11 == 0:
        quantity_of_decor += 2

    if day % 10 == 0:
        spirit -= 20  # cat
        cost += 5  # 1 Tree Skirt
        cost += 3  # 1 Tree Garland
        cost += 15  # 1 Tree Lights

        if day == days_left:
            spirit -= 30  # cat

    if day % 5 == 0:
        cost += 15 * quantity_of_decor  # Tree Lights
        spirit += 17  # Tree Lights

    if day % 5 == 0 and day % 3 == 0:
        spirit += 30

    if day % 3 == 0:
        cost += 5 * quantity_of_decor  # Tree Skirt
        cost += 3 * quantity_of_decor  # Tree Garland
        spirit += 3   # Tree Skirt
        spirit += 10  # Tree Garland

    if day % 2 == 0:
        cost += 2 * quantity_of_decor  # Ornament Set
        spirit += 5  # Ornament Set

print(f'Total cost: {cost}')
print(f'Total spirit: {spirit}')