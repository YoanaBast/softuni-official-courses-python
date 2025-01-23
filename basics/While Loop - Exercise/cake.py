cake_side_a = int(input())
cake_side_b = int(input())
pieces = cake_side_b * cake_side_a


command = input()

while command != 'STOP':
    eat_piece = int(command)
    pieces -= eat_piece

    if pieces <=0:
        break
    command = input()

if pieces <=0:
    print(f"No more cake left! You need {abs(pieces)} pieces more.")
else:
    print(f"{pieces} pieces are left.")