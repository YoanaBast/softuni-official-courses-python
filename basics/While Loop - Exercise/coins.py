resto = float(input())
coins = 0

while resto > 0:
    resto = round(resto, 2)

    if resto >=2:
        coins += 1
        resto -=2
    elif resto >=1:
        coins += 1
        resto -=1

    elif resto >= 0.50:
        resto -=0.50
        coins += 1
    elif resto >= 0.20:
        resto -= 0.20

        coins += 1
    elif resto >= 0.10:
        resto -= 0.10

        coins += 1
    elif resto >= 0.05:
        resto -= 0.05

        coins += 1
    elif resto >= 0.02:
        resto -= 0.02

        coins += 1
    elif resto >= 0.01:
        resto -= 0.01

        coins += 1

print(coins)