# Write a program that receives a single string (integers separated by a comma and space ", "),
# finds all the zeros, and moves them to the back without messing up the other elements. Print the resulting integer list.

input_list = input().split(", ")
nums_list = []
zero_count = 0
new_list = []

for x in input_list:
    nums_list.append(int(x))

for nums in nums_list:
    if nums > 0:
        new_list.append(nums)
    else:
        zero_count += 1

for y in range(zero_count):
    new_list.append(0)

print(new_list)


