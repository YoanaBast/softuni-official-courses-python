ban_list = input().split(', ')
text = input()

for word in ban_list:
    if word in text:
        text = text.replace(word, '*' * len(word))

print(text)