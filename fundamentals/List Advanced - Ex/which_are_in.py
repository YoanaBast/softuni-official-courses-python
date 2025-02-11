str_one = input().split(', ')
str_two = input().split(', ')
result = []
for item in str_one:
    for x in str_two:
        if item in x:
            result.append(item)
            break
print(result)