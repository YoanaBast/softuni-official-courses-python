cards_list = input().split(", ")
n = int(input())

for _ in range(n): ###
    command = input()
    command_split = command.split(", ")

    if command_split[0] == "Add":
        card_name = command_split[1]
        if card_name in cards_list:
            print("Card is already in the deck")
        else:
            cards_list.append(card_name)
            print("Card successfully added")

    elif command_split[0] == "Remove":
        card_name = command_split[1]
        if card_name in cards_list:
            cards_list.remove(card_name)
            print("Card successfully removed")
        else:
            print("Card not found")

    elif command_split[0] == "Remove At":
        index = int(command_split[1])
        if 0 <= index < len(cards_list): ###
            cards_list.pop(index)
            print("Card successfully removed")
        else:
            print("Index out of range")

    elif command_split[0] == "Insert":
        index = int(command_split[1])
        card_name = command_split[2]
        if 0 <= index <= len(cards_list):
            if card_name in cards_list:
                print("Card is already added")
            else:
                cards_list.insert(index, card_name)
                print("Card successfully added")
        else:
            print("Index out of range")

print(", ".join(cards_list))
