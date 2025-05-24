rows = int(input())
matrix = []
knights = {}
knight_key = ord('a') - 1
removed = 0

moves = {
    1: lambda r, c: (r - 1, c - 2),
    2: lambda r, c: (r - 2, c - 1),
    3: lambda r, c: (r - 2, c + 1),
    4: lambda r, c: (r - 1, c + 2),
    5: lambda r, c: (r + 1, c + 2),
    6: lambda r, c: (r + 2, c + 1),
    7: lambda r, c: (r + 2, c - 1),
    8: lambda r, c: (r + 1, c - 2),
}
# for row in range(rows):
#     data = [x for x in list(input())]
#     matrix.append(data)
#     for d in data:
#         if d == 'K':
#             knight_key += 1
#             # knights[chr(knight_key)] = {'r': row, 'c': data.index('K'), 'k': 0 }
#             knights[chr(knight_key)] = {'r': row, 'c': col, 'k': 0}
for row in range(rows):
    data = list(input())
    matrix.append(data)
    for col, d in enumerate(data):
        if d == 'K':
            knight_key += 1
            knights[chr(knight_key)] = {'r': row, 'c': col, 'k': 0}

while knights:
    for knight in knights:
        k_row, k_col = knights[knight]['r'], knights[knight]['c']
        for attack in moves:
            attack_r, attack_c = moves[attack](k_row, k_col)
            if 0 <= attack_r < rows and 0 <= attack_c < len(matrix[0]):
                if matrix[attack_r][attack_c] == 'K':
                    knights[knight]['k'] += 1
    #
    # any_k_positive = any(v['k'] > 0 for v in knights.values())
    # if not any_k_positive:
    #     break
    max_k = max(d['k'] for d in knights.values())
    if max_k == 0:
        break

    knights_with_max_k = [k for k, v in knights.items() if v['k'] == max_k]
    top_left = min(knights_with_max_k, key=lambda x: (knights[x]['r'], knights[x]['c']))

    rem_r, rem_c = knights[top_left]['r'], knights[top_left]['c']
    matrix[rem_r][rem_c] = '0'

    del knights[top_left]
    removed += 1

    for knight in knights:
        knights[knight]['k'] = 0

print(removed)