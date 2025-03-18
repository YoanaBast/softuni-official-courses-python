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
        if sym*6 in half1 and sym*6 in half2:
            result = f'ticket "{tick}" - 6{sym}'
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



