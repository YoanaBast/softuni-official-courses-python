my_dict = {}

def fill_the_list(num: int):
    index = int(input())
    for i in range(index):
        word1 = input()
        word2 = input()
        if word1 not in my_dict:
            my_dict[word1] = []
        if word2 not in my_dict:
            my_dict[word1].append(word2)
    return my_dict

def nice_print_key_value(dict_lookup: dict):
    result = []
    for key in dict_lookup:
        list_values = []
        for value1 in dict_lookup[key]:
            list_values.append(value1)
        result.append(f"{key} - {', '.join(list_values)}")
    return '\n'.join(result)

fill_the_list(my_dict)
print(nice_print_key_value(my_dict))
