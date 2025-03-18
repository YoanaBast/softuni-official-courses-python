ws = ['@', '#', '$', '^']
tickets = [ti.strip() for ti in input().split(", ")]

for ticket in tickets:
    if len(ticket) != 20:
        print('invalid ticket')
        continue
#Cas$$$$$$$ Ca$$$$$$s$
    else:
        half1, half2 = ticket[:10], ticket[10:]
        len4e = 1

        symindx = -1
        for sym in ws:
            symindx += 1
            if len4e >= 6:
                if len4e == 10:
                    print(f'ticket "{ticket}" - 10{ws[symindx-1]} Jackpot!')
                    break
                else:
                    print(f'ticket "{ticket}" - {len4e}{ws[symindx-1]}')
                    break

            counter1 = 1
            for index in range(len(half1) - 1, 0, -1):
                if half1[index] == sym:
                    if index > 0:
                        if half1[index] == half1[index - 1]:
                            counter1 += 1

            counter2 = 1
            for index in range(len(half2) - 1, 0, -1):
                if half2[index] == sym:
                    if index > 0:
                        if half2[index] == half2[index - 1]:
                            counter2 += 1

            len4e = counter1 if counter1 < counter2 else counter2

        if len4e < 6:
            print(f'ticket "{ticket}" - no match')



