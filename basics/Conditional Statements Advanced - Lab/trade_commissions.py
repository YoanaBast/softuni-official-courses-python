grad = input()
s = float(input()) #obem prodajbi
komis = 0

if grad == 'Sofia':
    if 0 <= s <= 500 and s > 0:
        komis = 0.05 * s
        print(f"{komis:.2f}")
    elif 500 < s <= 1000 and s > 0:
        komis = 0.07 * s
        print(f"{komis:.2f}")
    elif 1000 < s <= 10000 and s > 0:
        komis = 0.08 * s
        print(f"{komis:.2f}")
    elif s > 10000 and s > 0:
        komis = 0.12 * s
        print(f"{komis:.2f}")
    else:
            print('error')

elif grad == 'Varna':
    if 0 <= s <= 500 and s > 0:
        komis = 0.045 * s
        print(f"{komis:.2f}")
    elif 500 < s <= 1000 and s > 0:
        komis = 0.075 * s
        print(f"{komis:.2f}")
    elif 1000 < s <= 10000 and s > 0:
        komis = 0.10 * s
        print(f"{komis:.2f}")
    elif s > 10000 and s > 0:
        komis = 0.13 * s
        print(f"{komis:.2f}")
    else:
        print('error')
elif grad == 'Plovdiv':
    if 0 <= s <= 500 and s > 0:
        komis = 0.055 * s
        print(f"{komis:.2f}")
    elif 500 < s <= 1000 and s > 0:
        komis = 0.08 * s
        print(f"{komis:.2f}")
    elif 1000 < s <= 10000 and s > 0:
        komis = 0.12 * s
        print(f"{komis:.2f}")
    elif s > 10000 and s > 0:
        komis = 0.145 * s
        print(f"{komis:.2f}")
    else:
        print('error')
else:
    print('error')