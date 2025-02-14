quantity_of_decorations = int(input())
days_left_until_Christmas = int(input())

ornament_set = 0
tree_skirt = 0
tree_garland = 0
decoration = 0
tree_lights = 0
spirit = 0
price = 0



for days in range(1, days_left_until_Christmas + 1):

    if days % 11 == 0:
        quantity_of_decorations += 2

    if days % 10 == 0:
        spirit -= 20
        price += 5 + 3 + 15
        if days == days_left_until_Christmas:
            spirit -= 30  # cat

    if days % 5 == 0 and days % 3 == 0:
        spirit += 30

    if days % 2 == 0:
        ornament_set = quantity_of_decorations
        price += 2 * ornament_set
        spirit += 5
    if days % 5 == 0:
        tree_lights = quantity_of_decorations
        price += 15 * tree_lights
        spirit += 17

    if days % 3 == 0:
        tree_skirt = quantity_of_decorations
        price += 5 * tree_skirt
        spirit += 3
        tree_garland = quantity_of_decorations
        price += 3 * tree_garland
        spirit += 10

print(f"Total cost: {price}")
print(f"Total spirit: {spirit}")

