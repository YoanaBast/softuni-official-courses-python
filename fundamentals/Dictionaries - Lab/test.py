dict_lookup = {'cute': ['adorable ', 'charming '], 'smart': ['clever']}

result = []
for key in dict_lookup:
    list_values = []
    for value1 in dict_lookup[key]:
        list_values.append(value1)
    result.append(f"{key} - {', '.join(list_values)}")
print('\n'.join(result))