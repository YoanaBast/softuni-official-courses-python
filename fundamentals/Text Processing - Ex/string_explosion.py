explosion = input()
new_str = ''
strength = 0

for index in range(len(explosion)):
    if strength > 0 and explosion[index] != '>':
        strength -= 1
    elif explosion[index] == '>':
        new_str += '>'
        strength += int(explosion[index+1])
    else:
        new_str += explosion[index]

print(new_str)
