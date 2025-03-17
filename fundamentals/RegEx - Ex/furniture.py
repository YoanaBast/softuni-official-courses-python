import re
regex = r"(?P<item>(?<=>>)[A-Za-z]+)<<(?P<price>\d+[\.\d+]*)!(?P<quan>\d+)"
furniture = []
total = 0
while True:
    command = input()
    if command == 'Purchase':
        break

    match = re.search(regex, command)
    if match:
        item, price, quan = match.groups()
        furniture.append(item)
        total += float(price) * int(quan)

print("Bought furniture:")
for furn in furniture:
    print(furn)
    #  '\n'.join(furniture) was breaking judge for some reason
print(f'Total money spend: {total:.2f}')