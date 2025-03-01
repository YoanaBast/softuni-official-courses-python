cards_list = input().split(", ")
n = int(input())

for turn in range(1, n+1):
    command = input()
    command_split = command.split(', ')

    if command_split[0] == 'Add':
        card_name = command_split[1]
        if card_name in cards_list:
            print("Card is already in the deck")
        else:
            cards_list.append(card_name)
            print('Card successfully added')

    elif command_split[0] == 'Remove':
        card_name = command_split[1]
        if card_name in cards_list:
            cards_list.remove(card_name)
            print('Card successfully removed')
        else:
            print("Card not found")

    elif command_split[0] == 'Remove At':
        index = int(command_split[1])
        if index <= len(cards_list) -1 and index >= 0:
            cards_list.pop(index)
            print('Card successfully removed')
        else:
            print("Index out of range")

    elif command_split[0] == 'Insert':
        index = int(command_split[1])
        card_name = command_split[2]
        if card_name not in cards_list and index <= len(cards_list) -1 and index >= 0:
            cards_list.insert(index, card_name)
            print('Card successfully added')
        elif card_name in cards_list:
            print("Card is already added")
        elif index > len(cards_list) - 1 or index < 0:
            print("Index out of range")

print(', '.join(cards_list))