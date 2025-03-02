letters_count = {}

def fill_the_dict(input_str):
    words = input_str.split(' ')
    for word in words:
        for letter in word:
            if letter not in letters_count.keys():
                letters_count[letter] = 1
            else:
                letters_count[letter] += 1
    return letters_count

def format_print(sorted_dict: dict):
    result = []
    for key, value in sorted_dict.items():
        result.append(f"{key} -> {value}")
    return '\n'.join(result)

words = input()
fill_the_dict(words)
print(format_print(letters_count))