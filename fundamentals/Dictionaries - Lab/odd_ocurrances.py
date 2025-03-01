lowercase_list = (input().lower().split(' '))
dict = {}

def fill_dict(list_user):
    for i in list_user:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return list_user

def sort_odds():
    sorted = [i for i in dict if dict[i] % 2 != 0]
    return ' '.join(sorted)

fill_dict(lowercase_list)
result = sort_odds()

print(result)