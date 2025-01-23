budget = int(input())
season = input() #"Spring", "Summer", "Autumn" или "Winter";
fishermen = int(input())
ship_rent = 0
discount = 0
more_discount = 0

if season == 'Spring':
    ship_rent = 3000
elif season in ('Autumn', 'Summer'):
    ship_rent = 4200
elif season == 'Winter':
    ship_rent = 2600
if fishermen <= 6:
    discount = 0.10 * ship_rent
elif 7 <= fishermen <= 11:
    discount = 0.15 * ship_rent
elif fishermen >= 12:
    discount = 0.25 * ship_rent

if (fishermen > 0) and (fishermen % 2 == 0) and (season != 'Autumn'):
    more_discount = 0.05 * (ship_rent - discount)

total = (ship_rent - discount) - more_discount

if budget >= total:
    print(f"Yes! You have {budget-total:.2f} leva left.")
else:
    print(f"Not enough money! You need {total - budget:.2f} leva.")
