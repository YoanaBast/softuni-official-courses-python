
budget = float(input())
flour_price = float(input())
pack_eggs_price = 0.75 * flour_price
price_1l_milk = flour_price + flour_price * 0.25
price_250_milk = price_1l_milk * 0.25
bread_price = flour_price + pack_eggs_price + price_250_milk

colored_eggs = 0
third_bread = 0
eggs_lost = 0
breads_baked = 0
money_left = budget

while True:
    if money_left >= bread_price:
        breads_baked += 1
        colored_eggs += 3
        third_bread += 1
        money_left -= bread_price
        if third_bread % 3 == 0:
            eggs_lost += (breads_baked - 2)

    else:
        break

total_bread_cost = bread_price * breads_baked
left_money = budget - total_bread_cost
print(f"You made {breads_baked} loaves of Easter bread! Now you have {colored_eggs - eggs_lost} eggs and {left_money:.2f}BGN left.")
