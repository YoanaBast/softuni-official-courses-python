import re
regex = r"(?P<item>(?<=>>)[A-Za-z]+)<<(?P<price>\d+[\.\d+]*)!(?P<quan>\d+)"
furniture = []
total = 0
while True:
    command = input()
    if command == 'Purchase':
        break

    matches = re.finditer(regex, command)
    for match in matches:
        item = match.group('item')
        furniture.append(item)
        price = match.group('price')
        quan = match.group('quan')
        total += float(price) * float(quan)

print(furniture)
print(total)
print("Bought furniture:")
Sofa TV Total money spend: 2436.69