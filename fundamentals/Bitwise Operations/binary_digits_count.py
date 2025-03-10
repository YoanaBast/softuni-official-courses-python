def decimal_to_binary(num: int):
    binary = []
    while True:
        if num == 0:
            break
        if num % 2 == 0:
            binary.append(0)
            num = num // 2
        elif num % 2 == 1:
            binary.append(1)
            num = num // 2
    binary.reverse()
    result = binary
    return result

digi = int(input())
binary_num = decimal_to_binary(digi)

zeroes = 0
ones = 0
for num in binary_num:
    if num == 0:
        zeroes += 1
    elif num ==1:
        ones += 1
if zeroes > 0:
    print(f'We have {zeroes} zeroes.')
else:
    print(f'We have {ones} ones.')

