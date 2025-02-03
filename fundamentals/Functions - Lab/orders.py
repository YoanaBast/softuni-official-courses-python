# Write a function that calculates the total price of an order and returns it.
# The function should receive one of the following products: "coffee", "coke", "water", or "snacks", and a quantity of the product.
# The prices for a single piece of each product are:
# · coffee - 1.50
# · water - 1.00
# · coke - 1.40
# · snacks - 2.00
# Print the result formatted to the second decimal place.

def total(item, amount):
    prices =  {
    'coffee': 1.50,
    'water': 1.00,
    'coke': 1.40,
    'snacks': 2.00
    }
    return prices.get(item, 0) * amount

item1 = input()
amount1 = int(input())

result = total(item1, amount1)
print(f'{result:.2f}')