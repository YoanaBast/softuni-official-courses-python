cities_n = int(input())
total_profit = 0

for city in range(1, cities_n + 1):
    city_name = input()
    money_earned = float(input())
    expenses = float(input())


    if city % 5 == 0:
        money_earned -= money_earned * 0.1

    elif city % 3 == 0:
        expenses  += expenses * 0.5

    profit = money_earned - expenses
    total_profit += profit
    print(f"In {city_name} Burger Bus earned {profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")