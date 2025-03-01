stock_dict = {}


def stock_the_fridge(items: str):
    stock = items.split(' ')
    for i in range(0, len(stock), 2):
        key = stock[i]
        value = int(stock[i + 1])
        stock_dict[key] = value
    return stock_dict

def lookup(items: str):
    orders = items.split(' ')
    result = []
    for order in orders:
        if order in stock_dict:
            result.append(f'We have {stock_dict[order]} of {order} left')
        else:
            result.append(f"Sorry, we don't have {order}")
    return '\n'.join(result)

items_input = input()
lookup_input = input()
stock_the_fridge(items_input)
print(lookup(lookup_input))
