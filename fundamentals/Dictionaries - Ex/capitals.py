def nice_print_key_value(sorted_dict: dict):
    result = []
    for key, value in sorted_dict.items():
        result.append(f"{key} -> {value}")
    return '\n'.join(result)


countries_list = input().split(', ')
capitals_list = input().split(', ')
con_cap_dict = {country: capital for country,capital in zip(countries_list, capitals_list)}

print(nice_print_key_value(con_cap_dict))