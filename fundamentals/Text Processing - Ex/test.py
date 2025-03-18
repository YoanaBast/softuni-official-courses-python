# def check_ticket(ticket: str) -> str:
#     if len(ticket) != 20:
#         return "invalid ticket"
#     winning_symbols = ('@', '#', '$', '^')
#     left_part = ticket[:10]
#     right_part = ticket[10:]
#     for current_winning_symbol in winning_symbols:
#         for uninterrupted_match_length in range(10, 5, -1):
#             winning_symbol_repetition = current_winning_symbol * uninterrupted_match_length
#             # Case where we have winning ticket
#             if winning_symbol_repetition in left_part and \
#                     winning_symbol_repetition in right_part:
#                 # Jackpot case
#                 if uninterrupted_match_length == 10:
#                     return f'ticket "{ticket}" - {uninterrupted_match_length}{current_winning_symbol} Jackpot!'
#                 # Winning ticket, no Jackpot
#                 return f'ticket "{ticket}" - {uninterrupted_match_length}{current_winning_symbol}'
#     return f'ticket "{ticket}" - no match'
#
#
# tickets = [ticket.strip() for ticket in input().split(", ")]
# for current_ticket in tickets:
#     print(check_ticket(current_ticket))
# ws = ('@', '#', '$', '^')
#
# ticket = 'Cas$$$$$$$Ca$$$$$$s$'
# half1, half2 = ticket[:10], ticket[10:]
# print(half1, half2)
#
# result = f'ticket "{ticket}" - no match'
# half1, half2 = ticket[:10], ticket[10:]
#
# for sym in ws:
#     print(sym*10)
#     if sym * 10 in half1 and half2 == half1:
#         result = f'ticket "{ticket}" - 10{sym} Jackpot!'
#         break
#     if sym * 6 in half1 and sym * 6 in half2:
#         result = f'ticket "{ticket}" - 6{sym}'
#         break
half1 = "Cas$$$$$$$"
half2 = "Ca$$$$$$s$"
sym = '$'

# max_count_half1 = 0
# current_count_half1 = 0
# for char in half1:
#     if char == sym:
#         current_count_half1 += 1
#         max_count_half1 = max(max_count_half1, current_count_half1)
#     else:
#         current_count_half1 = 0

half2 = "Ca$$$$$$s$"
sym = '$'

duplicate = 1
for index in range(len(half2)-1, 0, -1):
    if half2[index] == sym:
        if index > 0:
            if half2[index] ==  half2[index-1]:
                duplicate += 1


# The max() function returns the item with the highest value

len4e = min(max_count_half1, max_count_half2)