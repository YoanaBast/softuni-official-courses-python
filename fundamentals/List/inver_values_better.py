#this is a better solution of invert_values

stringche_ot_usera = input()

my_list = stringche_ot_usera.split()

reverse_list = []

for num in my_list:
    rev_num = -int(num)
    reverse_list.append(rev_num)

print(reverse_list)