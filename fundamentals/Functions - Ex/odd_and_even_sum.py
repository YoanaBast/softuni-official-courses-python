def sums(number: str) -> str:
    odd_sum, even_sum = 0, 0

    listcho = []
    for index in range(len(number)):
        listcho.append(n[index])

    int_list = [int(listcho[xedni]) for xedni in range(len(number))]

    for num in int_list:
        if num % 2 == 0:
            even_sum += num
        elif num % 2 != 0:
            odd_sum += num
        else:
            continue

    result = f'Odd sum = {odd_sum}, Even sum = {even_sum}'
    return result

n = input()

print(sums(n))

