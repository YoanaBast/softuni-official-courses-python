stock = {}


def nice_print_key_value(my_dict: dict):
    result = []
    for key, value in my_dict.items():
        result.append(f"{key}: {value}")
    return '\n- '.join(result)

def get_statistics():
    total_prod = len(stock)
    total_quan = sum(stock.values())
    result = f"Products in stock:\n- " + nice_print_key_value(stock) + f"\nTotal Products: {total_prod}" f"\nTotal Quantity: {total_quan}"
    return result


while True:
    command = input()
    if command == 'statistics':
        print(get_statistics())
        break
    else:
        key, value = command.split(': ')
        if key not in stock:
            stock[key] = int(value)
        else:
            stock[key] += int(value)
