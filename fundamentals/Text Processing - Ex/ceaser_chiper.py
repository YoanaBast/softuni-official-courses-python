message = input()
new_msg = ''
for char in message:
    new_ord = ord(char) + 3
    new_char = chr(new_ord)
    new_msg += new_char
print(new_msg)