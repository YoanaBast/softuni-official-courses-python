nums_list = list(map(int, input().split(", ")))
found_indices = list(map(lambda x: x if nums_list[x] % 2 == 0 else 'no', range(len(nums_list))))
even_indc = list(filter(lambda a: a != 'no', found_indices))
print(even_indc)

