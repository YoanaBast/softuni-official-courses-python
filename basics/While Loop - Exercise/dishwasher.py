bottle = 750
plate = 5
pot = 15
round = 1
washed_pot = 0
washed_plate = 0

bottles_used = int(input())

command = input()
while command != 'End':
    count = int(command)
    round += 1
    if round % 3 == 0:
        washed_pot_ml = count * pot
        washed_pot = count
        washed_pot += washed_pot

    else:
        washed_plate_ml = count * plate
        washed_plate = count * plate
        washed_plate += washed_plate

    command = input()

total = washed_pot_ml + washed_plate_ml
diff = (bottles_used * bottle) - total

if diff >= 0:
    print("Detergent was enough!")
    print(f'{washed_plate} dishes and {washed_pot} pots were washed.')
    print(f'Leftover detergent {diff} ml.')
else:
    print("Not enough detergent, {abs(diff)} ml. more necessary!")
