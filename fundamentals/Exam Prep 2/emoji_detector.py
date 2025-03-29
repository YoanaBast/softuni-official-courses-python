import re
string4e = input()

regex_word = r"([:|*]{2})(?P<emoji>[A-Z]{1}[a-z]{2,})(\1)"
regex_int = r"\d"

emoji_dict = {}
matches = re.finditer(regex_word, string4e)
for match in matches:
    emoji_dict[match.group('emoji')] = [match.group(1), 0]
digi = re.findall(regex_int, string4e)

cool_threshold = 1
for dig in digi:
    cool_threshold *= int(dig)

for emo in emoji_dict.keys():
    ascii_sum = 0
    for char in emo:
        ascii_sum += ord(char)
    emoji_dict[emo][1] += ascii_sum

count_of_all_emojis = len(emoji_dict)


print(f"Cool threshold: {cool_threshold}")
print(f"{count_of_all_emojis} emojis found in the text. The cool ones are:")

emoji_dict_copy = {}
for key in emoji_dict.keys():
    if emoji_dict[key][1] >= cool_threshold:
        emoji_dict_copy[key] = emoji_dict[key]

for key in emoji_dict_copy.keys():
    print(f"{emoji_dict[key][0]}{key}{emoji_dict[key][0]}")