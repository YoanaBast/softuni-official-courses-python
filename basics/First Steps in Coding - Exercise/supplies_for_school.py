pack_pens = 5.80
pack_mark = 7.20
solution_per_lit = 1.20

pack_pens_count = int(input())
pack_mark_count = int(input())
solution_lit_count = int(input())
discount = int(input())

total = ((pack_pens_count * pack_pens) + (pack_mark_count * pack_mark) + (solution_lit_count * solution_per_lit))
final = total - total * discount / 100
print(final)

