strings = input().split()
str1_digits = [ord(char) for char in strings[0]]
str_2_digi = [ord(char) for char in strings[1]]
str1_longer =  False
str2_longer = False
total_sum = 0

if len(str1_digits) > len(str_2_digi):
    longer = len(str1_digits)
    shorter = len(str_2_digi)
    str1_longer = True

else:
    longer = len(str_2_digi)
    shorter = len(str1_digits)
    str2_longer = True

for operation in range(shorter):
    total_sum += str1_digits[0] * str_2_digi[0]
    str1_digits.pop(0)
    str_2_digi.pop(0)

if str1_longer:
    while len(str1_digits) > 0:
        total_sum += str1_digits[0]
        str1_digits.pop(0)
else:
    while len(str_2_digi) > 0:
        total_sum += str_2_digi[0]
        str_2_digi.pop(0)
print(total_sum)