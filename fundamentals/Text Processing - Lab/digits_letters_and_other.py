stringche = input()
let, digi, other = '', '', ''

for char in stringche:
    if char.isalpha():
        let += char
    elif char.isdigit():
        digi += char
    else:
        other += char

print(f"{digi}\n{let}\n{other}")
