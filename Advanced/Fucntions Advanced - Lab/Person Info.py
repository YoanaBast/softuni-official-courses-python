def get_info(name, age, town):

    result = f"This is {name} from {town} and he is {age} years old"
    return result


kwargs = {'name': 'Yoana', 'age': 24, 'town': 'Varna'}

print(get_info(**kwargs))