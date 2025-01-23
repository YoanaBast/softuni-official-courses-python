gradusi = int(input())
time = input()
obleklo = ''
obuvki = ''
if time == 'Morning':
    if 10 <= gradusi <= 18:
        obleklo = 'Sweatshirt'
        obuvki = 'Sneakers'
    elif 18 < gradusi <= 24:
        obleklo = 'Shirt'
        obuvki = 'Moccasins'
    elif gradusi >= 25:
        obleklo = 'T-Shirt'
        obuvki = 'Sandals'

    print(f"It's {gradusi} degrees, get your {obleklo} and {obuvki}.")

elif time == 'Afternoon':
    if 10 <= gradusi <= 18:
        obleklo = 'Shirt'
        obuvki = 'Moccasins'
    elif 18 < gradusi <= 24:
        obleklo = 'T-Shirt'
        obuvki = 'Sandals'
    elif gradusi >= 25:
        obleklo = 'Swim Suit'
        obuvki = 'Barefoot'

    print(f"It's {gradusi} degrees, get your {obleklo} and {obuvki}.")

elif time == 'Evening':
    if 10 <= gradusi <= 18:
        obleklo = 'Shirt'
        obuvki = 'Moccasins'
    elif 18 < gradusi <= 24:
        obleklo = 'Shirt'
        obuvki = 'Moccasins'
    elif gradusi >= 25:
        obleklo = 'Shirt'
        obuvki = 'Moccasins'

    print(f"It's {gradusi} degrees, get your {obleklo} and {obuvki}.")