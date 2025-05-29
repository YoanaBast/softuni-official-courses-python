def even_odd_filter(**kwargs):
    new_dict = {}
    for key, lst in kwargs.items():
        if key =='even':
            new_dict[key] = [x for x in lst if x % 2 == 0]
        else:
            new_dict[key] = [x for x in lst if x % 2 != 0]

    return dict(sorted(new_dict.items(), key=lambda z: -len(z[1])))



print(even_odd_filter(
odd=[1, 2, 3, 4, 10, 5],
even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))



print(even_odd_filter(

odd=[2, 2, 30, 44, 10, 5],

))