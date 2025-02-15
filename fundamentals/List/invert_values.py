# Write a program that receives a single string containing positive and negative numbers separated by a single space.
# Print a list containing the opposite of each number.

stringche_ot_usera = input()

my_list = stringche_ot_usera.split()

reverse_list = []

for index in range(len(my_list) -1, -1, -1):
    item = my_list[index]
    reverse_item = -int(item)
    reverse_list.append(reverse_item)

reverse_list.reverse()
print(reverse_list)

