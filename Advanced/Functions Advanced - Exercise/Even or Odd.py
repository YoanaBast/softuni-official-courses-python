def even_odd(*args):
    nums = [n for n in args if isinstance(n, int)]
    command = args[-1]

    if command == 'even':
        nums = list(filter(lambda x: x % 2 == 0, nums))
    else:
        nums = list(filter(lambda x: x % 2 != 0, nums))

    return nums


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
