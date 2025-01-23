vnoski = input()
total_sum = 0

while vnoski != 'NoMoreMoney':
    number = float(vnoski)
    if float(vnoski) < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {number:.2f}")
    total_sum += number
    vnoski = input()
print(f'Total: {total_sum:.2f}')


