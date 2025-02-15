gifts = input().split()

while True:
    command = input()

    if command == 'No Money':
        break
    else:
        gift = command.split() #eggs
        command = gift.pop(0) #outofstock
        if command == 'OutOfStock':
            gift = gift[0]  # eggs but as str
            while gifts.count(gift) > 0:
                index = gifts.index(gift)
                gifts[index] = 'None'

        elif command == 'Required':
            index_2 = int(gift[1])
            gift = gift[0]  # eggs but as str
            if len(gifts) >= index_2 and index_2 >= 0: # INDEX >= 0 !!
                gifts[index_2] = gift

        elif command == 'JustInCase':
            gift = gift[0]
            gifts[-1] = gift

gifts = list(filter(lambda x: x != 'None', gifts))
print(*gifts)