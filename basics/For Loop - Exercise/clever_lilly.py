age = int(input())
wash_price = float(input())
toy_price = int(input())
total_money = 0
total_toys = 0

for bd in range(1, age + 1):
    if bd % 2 == 0:
        total_money += bd * 5
        total_money -= 1

    else:
        total_toys += 1

total_toys_money = toy_price * total_toys
final_money = total_money + total_toys_money

if final_money >= wash_price:
    diff = final_money - wash_price
    print(f"Yes! {diff:.2f}")
else:
    diff = wash_price - final_money
    print(f"No! {diff:.2f}")