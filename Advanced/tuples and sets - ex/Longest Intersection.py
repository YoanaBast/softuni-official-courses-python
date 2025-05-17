n = int(input())
longest = []
for _ in range(n):
    #"{first_start},{first_end}-{second_start},{second_end}
    first_r, second_r = input().split('-') #[{first_start},{first_end}],

    first_start, first_end = first_r.split(',')
    second_start, second_end = second_r.split(',')

    first_set = set()
    second_set = set()

    for x in range(int(first_start), int(first_end)+1):
        first_set.add(x)
    for y in range(int(second_start), int(second_end)+1):
        second_set.add(y)
    inter = first_set & second_set
    if len(inter) > len(longest):
        longest = inter

print(f'Longest intersection is {list(longest)} with length {len(longest)}')