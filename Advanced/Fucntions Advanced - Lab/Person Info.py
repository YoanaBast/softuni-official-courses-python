def get_info(**kwargs):
    n, t, a = kwargs['name'],kwargs['town'],kwargs['age'],

    return f"This is {n} from {t} and he is {a} years old"



print(get_info(name='Yoana', age=24, town= 'Varna'))