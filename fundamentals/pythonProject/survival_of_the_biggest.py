# Write a program that receives a list of integer numbers (separated by a single space) and a number n.
# The number n represents the count of numbers to remove from the list.
# You should remove the smallest ones, and then, you should print all the numbers that are left in the list,
# separated by a comma and a space ", ".

str_of_nums = input().split()
list_of_int_nums = []
for i in range(len(str_of_nums)):
    int_item = int(str_of_nums[i])
    list_of_int_nums.append(int_item)

count_to_remove = int(input())

for index in range(count_to_remove):
    smallest = min(list_of_int_nums)
    list_of_int_nums.remove(smallest)

# print(", ".join(map(str, list_of_int_nums)))
print(*list_of_int_nums, sep=", ")