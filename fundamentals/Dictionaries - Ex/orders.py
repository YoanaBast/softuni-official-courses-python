# {beer}: {{price: 0} {quantity: 0}}
menu = {}


def nice_print(dict_lookup: dict):
    result = []
    for key in dict_lookup: #beer, nukacola
        price = dict_lookup[key]['price']
        quantity = dict_lookup[key]['quantity']
        item_total = quantity * price
        result.append(f"{key} -> {item_total:.2f}")
    return '\n'.join(result)


while True:
    command = input()
    if command == 'buy':
        break
    name, price, quantity = command.split()
    if name not in menu:
        menu[name] = {'price': float(price), 'quantity': int(quantity)}
    else:
        menu[name]['price'] = float(price)
        menu[name]['quantity'] += int(quantity)

print(nice_print(menu))