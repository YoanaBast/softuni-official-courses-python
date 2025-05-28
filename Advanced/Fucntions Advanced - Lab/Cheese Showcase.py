def sorting_cheeses(**kwargs):
    result = []
    for key in kwargs.keys():
        kwargs[key] = sorted(kwargs[key], reverse=True)

    sorted_cheeses = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]) )

    for item, value in sorted_cheeses:
        result.append(item)
        result.extend((str(v) for v in value))

    return "\n".join(result)

#LUBE

print(

sorting_cheeses(

Parmigiano=[165, 215],

Feta=[150, 515],

Brie=[150, 125]

)

)
