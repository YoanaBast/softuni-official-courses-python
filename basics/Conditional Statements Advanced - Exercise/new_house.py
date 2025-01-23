flower_type = input() #текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
flower_amount = int(input())
budget = int(input())

price_roses = 5.00
price_dahlias = 3.80
price_tulips = 2.80
price_narcissus = 3.00
price_gladiolus = 2.50

total_price: int = 0

if flower_type == 'Roses':
    if flower_amount > 80:
        total_price = 0.90 * price_roses * flower_amount
    else:
        total_price = price_roses * flower_amount

elif flower_type == 'Dahlias':
    if flower_amount > 90:
        total_price = 0.85 * price_dahlias * flower_amount
    else:
        total_price = price_dahlias * flower_amount

elif flower_type == 'Tulips':
    if flower_amount > 80:
        total_price = 0.85 * price_tulips * flower_amount
    else:
        total_price = price_tulips * flower_amount
elif flower_type == 'Narcissus':
    if flower_amount < 120:
        total_price = 1.15 * price_narcissus * flower_amount
    else:
        total_price =price_narcissus * flower_amount
elif flower_type == 'Gladiolus':
    if flower_amount < 80:
        total_price = 1.20 * price_gladiolus * flower_amount
    else:
        total_price = price_gladiolus * flower_amount

if budget >= total_price:
    print(f"Hey, you have a great garden with {flower_amount} {flower_type} and {budget - total_price:.2f} leva left.")
elif budget < total_price:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")

