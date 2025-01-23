box_volume = 1*1*1  # meters
space_a = int(input())
space_b = int(input())
space_c = int(input())
space_volume = space_c * space_b * space_a
command = input()
moved_boxes = 0

while command != 'Done':
    command_number = int(command)
    box_volume_moved = command_number * box_volume
    moved_boxes += box_volume_moved


    if space_volume <= moved_boxes:
        break

    command = input()

if space_volume <= moved_boxes:
    print(f'No more free space! You need {abs(space_volume - moved_boxes)} Cubic meters more.')
else:
    print(f"{space_volume - moved_boxes} Cubic meters left.")
