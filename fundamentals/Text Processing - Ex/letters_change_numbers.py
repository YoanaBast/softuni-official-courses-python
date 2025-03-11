strings = input().split() #d7k l89L o7T
total = 0

for string in strings: #d7k
    number_str = ''
    result = 0
    for index in range(len(string)): # 0 1 2
        if string[index].isdigit():
            number_str += string[index]
    number = int(number_str)
    first_let = string[0]
    last_let = string[-1]

    if first_let.isupper():
        first_let_position = ord(first_let) - 64
        result = number / first_let_position
    elif first_let.islower():
        first_let_position = ord(first_let) - 96
        result = number * first_let_position

    if last_let.isupper():
        last_let_position = ord(last_let) - 64
        result -= last_let_position
    elif last_let.islower():
        last_let_position = ord(last_let) - 96
        result += last_let_position
    total += result

print(f"{total:.2f}")