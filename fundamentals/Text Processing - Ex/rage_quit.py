rage_str = input() #aSd2&5s@1
super_rage_str = ''
sub_string = ""
repetitions = ""

for index in range(len(rage_str)):
    if not rage_str[index].isdigit():
        sub_string += rage_str[index].upper()
    else:
        for next_index in range(index, len(rage_str)):
            if not rage_str[next_index].isdigit():
                break
            repetitions += rage_str[next_index]
        super_rage_str += sub_string * int(repetitions)
        sub_string = ""
        repetitions = ""

print(f"Unique symbols used: {len(set(super_rage_str))}")
print(super_rage_str)