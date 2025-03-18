tickets = [ti.strip() for ti in input().split(", ")]
w1, w2, w3, w4  = '@'*6, '#'*6, '$'*6, '^'*6
j1, j2, j3, j4 = '@'*20, '#'*20, '$'*20, '^'*20

for ticket in tickets:
    if len(ticket) != 20:
        print('invalid ticket')
        continue

    if ticket in (j1, j2, j3, j4):
        print(f'ticket "{ticket}" - 10{ticket[1]} Jackpot!')
        continue

    half1, half2 = ticket[:11], ticket[10:]
    if all(w not in half1 for w in [w1, w2, w3, w4]):
        print(f'ticket "{ticket}" - no match')
        continue

    if all(w not in half2 for w in [w1, w2, w3, w4]):
        print(f'ticket "{ticket}" - no match')
        continue

    symbol = [char for char in ticket if not char.isalpha()]
    sw = symbol[0]
    print(f'ticket "{ticket}" - 6{sw}')