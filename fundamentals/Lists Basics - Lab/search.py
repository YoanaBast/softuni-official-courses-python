# On the first line, you will receive a number n.
# On the second line, you will receive a word.
# On the following n lines, you will be given some strings.
# You should add them to a list and print them.
# After that, you should filter out only the strings that include the given word and print that list too.

n = int(input())
word = input()
my_list = []
for _ in range(n):
    some_string = input()
    my_list.append(some_string)

print(my_list)

for index in range(len(my_list) -1, -1, -1):
    item = my_list[index]

    if word not in item:
        my_list.remove(item)

print(my_list)

