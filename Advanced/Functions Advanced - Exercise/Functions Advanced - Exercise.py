def neg_pos(*args):
    result = ''
    negative = sum([x for x in args if x < 0])
    positive = sum([y for y in args if y >= 0])
    result += str(negative)
    result += f'\n{str(positive)}'

    if abs(negative) > abs(positive):
        result += f'\nThe negatives are stronger than the positives'
    else:
        result += f'\nThe positives are stronger than the negatives'
    return result

nums = [int(x) for x in input().split()]
print(neg_pos(*nums))