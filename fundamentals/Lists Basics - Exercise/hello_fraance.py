items_price = input().split('|')
budget = float(input())
markup = 0
profit = 0
markup_list = []
for x in items_price:

    if budget == 0:
        break

    item, price = x.split('->')
    price = float(price)

    if item == 'Clothes' and price <= 50.00:
        if budget >= price:
            budget -= price
            markup += price * 1.40
            markup_list.append(markup)
            profit += markup - price
            markup = 0
        else:
            continue

    elif item == 'Shoes' and price <= 35.00:
        if budget >= price:
            budget -= price
            markup += price * 1.40
            markup_list.append(markup)
            profit += markup - price
            markup = 0
        else:
            continue

    elif item == 'Accessories' and price <= 20.50:
        if budget >= price:
            budget -= price
            markup += price * 1.40
            markup_list.append(markup)
            profit += markup - price
            markup = 0
        else:
            continue


for markedup in markup_list:
    print(f'{markedup:.2f}', end=' ')

print()
print(f'Profit: {profit:.2f}')

if budget + sum(markup_list) >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')