def nice_print(dict_lookup: dict):
    result = []
    for key in dict_lookup:
        result.append(f"{key} -> Composer: {dict_lookup[key][0]}, Key: {dict_lookup[key][1]}")
    return('\n'.join(result))

initial_n_pieces = int(input())
pieces_dict = {}

for _ in range(initial_n_pieces):
    piece, composer, key = input().split("|")  # "{piece}|{composer}|{key}
    pieces_dict[piece] = [composer, key]

while True:
    command = input().split("|")
    if command[0] == 'Stop':
        print(nice_print(pieces_dict))
        break

    elif command[0] == 'Add':  # "Add|{piece}|{composer}|{key}
        piece, composer, key = command[1], command[2], command[3]
        if piece not in pieces_dict.keys():
            pieces_dict[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f'{piece} is already in the collection!')

    elif command[0] == 'Remove':  # "Remove|{piece}
        piece = command[1]
        if piece in pieces_dict.keys():
            del pieces_dict[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command[0] == 'ChangeKey':  # ChangeKey|{piece}|{new key}
        piece, new_key = command[1], command[2]
        if piece in pieces_dict.keys():
            pieces_dict[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
