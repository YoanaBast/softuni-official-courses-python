# Write a program that reads a sequence of strings, separated by a single space.
# Each string should be repeated N times, where N is the length of the string.
# Print the final strings concatenated into one string.
def my_function(some_list: list):
    result = []
    for item in some_list:
        lenght = len(item)
        current_res = ''.join(item * lenght)
        result.append(current_res)
    return ''.join(result)

init_str = input().split()
uwu = my_function(init_str)
print(uwu)