# 5. Special Numbers
#
# Write a program that reads an integer n.
# Then, for all numbers in the range [1, n], print the number and if it is special or not (True / False).
# A number is special when the sum of its digits is 5, 7, or 11.
# n = int(input())
# for num in range(1, n + 1):
#     sum_of_digits = 0
#     digits = num
#
#     while digits > 0:
#         sum_of_digits += digits % 10
#         digits = int(digits / 10)
#
#         if (sum_of_digits == 5) or (sum_of_digits == 7) or (sum_of_digits == 11):
#             print(f'{num} -> True')
#         else:
#             print(f'{num} -> False')
# tuka osrah indenta i while loopa mi runnva 2 puti za 2 digit nums

n = int(input())

for num in range(1, n + 1):
    sum_of_digits = 0
    digits = num


    while digits > 0:
        sum_of_digits += digits % 10
        digits = int(digits / 10)

    if (sum_of_digits == 5) or (sum_of_digits == 7) or (sum_of_digits == 11):
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')