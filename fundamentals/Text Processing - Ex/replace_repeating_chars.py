message = input()
last = ''
new_msg = ''

for char in message:
    if char != last:
        new_msg += char
    last = char

print(new_msg)

