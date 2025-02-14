stado = input().split(', ')
stado.reverse()
if stado[0] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    position = 0
    for animal in stado:
        if animal == 'sheep':
            position += 1
        if animal == 'wolf':
            print(f"Oi! Sheep number {position}! You are about to be eaten by a wolf!")
            break

