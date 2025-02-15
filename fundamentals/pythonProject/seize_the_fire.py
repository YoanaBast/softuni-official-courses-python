
cell_and_water_needed = input().split('#')
water = int(input())
cells = []
effort = 0

for item in cell_and_water_needed:
    if water == 0:
        break

    key, value = item.split(" = ")
    value = int(value)
    if key == 'High' and value in range(81, 125 + 1):
        if water >= value:
            water -= value
            cells.append(value)
            effort += 0.25 * value
        else:
            continue

    elif key == 'Medium' and value in range(51, 80 + 1):
        if water >= value:
            water -= value
            cells.append(value)
            effort += 0.25 * value
        else:
            continue

    elif key == 'Low' and value in range(1, 50 + 1):
        if water >= value:
            water -= value
            cells.append(value)
            effort += 0.25 * value
        else:
            continue

print('Cells:')
for cell in cells:
    print(f'- {cell}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {sum(cells)}')


