# n = int(input())
#
# for row in range(1, n + 1):
#     for col in range(1, row + 1):
#         if current > n:
#             is_current_bigger_than_n = True
#             break
#         print(str(current) + ' ', end='')
#         current += 1
#     if is_current_bigger_than_n:
#         break
#     print()

for number in range(first_num, second_num + 1):
    number_to_str = str(number)
    even_sum = 0
    odd_sum = 0

    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(number, end=' ')