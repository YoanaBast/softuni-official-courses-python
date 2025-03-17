rage_str = input()  # aSd2&5s@1
super_rage_str = ''
for_loop = len(rage_str)

for index in range(for_loop):  # 0, 1, 2, ...9
    if rage_str[index].isdigit():  # aSd2&5s@1[index]
        amount = int(rage_str[index])  # 2
        letters = rage_str[:index]  # aSd
        if '-' in letters:
            letters = letters.replace('Ʊ', '')

        super_rage_str += letters.upper() * amount
        rage_str = rage_str.replace(letters, 'Ʊ' * len(letters))
        rage_str = rage_str.replace(rage_str[index], 'Ʊ')
        letters = ''
        static_len = 0

unique_count = len(set(super_rage_str))

print(f'Unique symbols used: {unique_count}')
print(super_rage_str)