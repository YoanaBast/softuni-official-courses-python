chicken_price = 10.35
fish_price = 12.40
vege_price = 8.15

chicken_count = int(input("Chicken: "))
fish_count = int(input("Fish: "))
vege_count = int(input("Veg: "))

meals = (chicken_count * chicken_price) + (fish_count * fish_price) + (vege_count * vege_price)
dessert = 0.20 * meals
delivery = 2.50

total = meals + dessert + delivery
print(total)
