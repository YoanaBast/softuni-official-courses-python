product = input()
city = input()
amount = float(input())
coffee_price = 0
water_price = 0
beer_price = 0
sweets_price = 0
peanuts_price = 0

if city == "Sofia":
    coffee_price = 0.50
    water_price = 0.80
    beer_price = 1.20
    sweets_price = 1.45
    peanuts_price = 1.60
    if product == 'coffee':
        print(coffee_price * amount)
    elif product == 'water':
        print(water_price * amount)
    elif product == 'beer':
        print(beer_price * amount)
    elif product == 'sweets':
        print(sweets_price * amount)
    elif product == 'peanuts':
        print(peanuts_price * amount)
elif city == "Plovdiv":
    coffee_price = 0.40
    water_price = 0.70
    beer_price = 1.15
    sweets_price = 1.30
    peanuts_price = 1.50
    if product == 'coffee':
        print(coffee_price * amount)
    elif product == 'water':
        print(water_price * amount)
    elif product == 'beer':
        print(beer_price * amount)
    elif product == 'sweets':
        print(sweets_price * amount)
    elif product == 'peanuts':
        print(peanuts_price * amount)
elif city == "Varna":
    coffee_price = 0.45
    water_price = 0.70
    beer_price = 1.10
    sweets_price = 1.35
    peanuts_price = 1.55
    if product == 'coffee':
        print(coffee_price * amount)
    elif product == 'water':
        print(water_price * amount)
    elif product == 'beer':
        print(beer_price * amount)
    elif product == 'sweets':
        print(sweets_price * amount)
    elif product == 'peanuts':
        print(peanuts_price * amount)
