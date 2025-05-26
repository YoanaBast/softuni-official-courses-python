def sorting_cheeses(**kwargs):
    result = []
    mid = {}
    for key, value in kwargs.items():
        mid[key] = sorted(value, reverse=True) #{'Parmesan': [135, 120, 102], 'Camembert': [500, 430, 105, 100, 100], 'Mozzarella': [125, 50]}

    sorted_cheeses = dict(sorted(mid.items(), key=lambda item: len(item[1]), reverse=True))

    for item, value in sorted_cheeses.items():
        result.append(item)
        result.extend((str(v) for v in value))

    return "\n".join(result)


print(sorting_cheeses(Parmesan=[102, 120, 135], Camembert=[100, 100, 105, 500, 430], Mozzarella=[50, 125],))

