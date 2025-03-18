ws = ('@', '#', '$', '^')


def check_len(tick: str):
    result = 'Valid'
    if len(tick) != 20:
        result = 'invalid ticket'
    return result


def sym_check(tick: str):
    result = f'ticket "{tick}" - no match'
    half1, half2 = tick[:10], tick[10:]

    for sym in ws:
        if sym*10 in half1 and half2 == half1:
            result = f'ticket "{tick}" - 10{sym} Jackpot!'
            break

        max_count_half1 = 0
        current_count_half1 = 0
        for char in half1:
            if char == sym:
                current_count_half1 += 1
                max_count_half1 = max(max_count_half1, current_count_half1)
            else:
                current_count_half1 = 0

        max_count_half2 = 0
        current_count_half2 = 0
        for char in half2:
            if char == sym:
                current_count_half2 += 1
                max_count_half2 = max(max_count_half2, current_count_half2)
            else:
                current_count_half1 = 0
        #The max() function returns the item with the highest value

        len4e = min(max_count_half1, max_count_half2)

        if sym*6 in half1 and sym*6 in half2:
            result = f'ticket "{tick}" - {len4e}{sym}'
            break

    return result


tickets = [ti.strip() for ti in input().split(", ")]

for ticket in tickets:
    validity = check_len(ticket)
    if validity == 'invalid ticket':
        print(validity)
        continue

    result = sym_check(ticket)
    print(result)



