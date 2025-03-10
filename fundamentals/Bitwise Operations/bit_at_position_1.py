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
    while len(binary) < 8:
        binary.append(0)
    result = binary
    return result

numb = int(input())
binary_numb_list = decimal_to_binary(numb)
position_1 = binary_numb_list[1]
print(position_1)

#  Write a program that prints the bit at position 1 of the given integer. We use the standard counting: from right to left, starting from 0.