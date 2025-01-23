plod = input()
den = input()
amount = float(input())

price_banana = 0
price_apple = 0
price_orange = 0
price_grapefruit = 0
price_kiwi = 0
price_pineapple = 0
price_grapes = 0

if den in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'):
    price_banana = 2.50
    price_apple = 1.20
    price_orange = 0.85
    price_grapefruit = 1.45
    price_kiwi = 2.70
    price_pineapple = 5.50
    price_grapes = 3.85
    if plod == 'banana':
        print(f"{price_banana * amount:.2f}")
    elif plod == 'apple':
        print(f"{price_apple * amount:.2f}")
    elif plod == 'orange':
        print(f"{price_orange * amount:.2f}")
    elif plod == 'grapefruit':
        print(f"{price_grapefruit * amount:.2f}")
    elif plod == 'kiwi':
        print(f"{price_kiwi * amount:.2f}")
    elif plod == 'pineapple':
        print(f"{price_pineapple * amount:.2f}")
    elif plod == 'grapes':
        print(f"{price_grapes * amount:.2f}")
    else:
        print('error')
elif den in ('Saturday', 'Sunday'):
    price_banana = 2.70
    price_apple = 1.25
    price_orange = 0.90
    price_grapefruit = 1.60
    price_kiwi = 3.00
    price_pineapple = 5.60
    price_grapes = 4.20
    if plod == 'banana':
        print(f"{price_banana * amount:.2f}")
    elif plod == 'apple':
        print(f"{price_apple * amount:.2f}")
    elif plod == 'orange':
        print(f"{price_orange * amount:.2f}")
    elif plod == 'grapefruit':
        print(f"{price_grapefruit * amount:.2f}")
    elif plod == 'kiwi':
        print(f"{price_kiwi * amount:.2f}")
    elif plod == 'pineapple':
        print(f"{price_pineapple * amount:.2f}")
    elif plod == 'grapes':
        print(f"{price_grapes * amount:.2f}")
    else:
        print('error')
else:
    print('error')