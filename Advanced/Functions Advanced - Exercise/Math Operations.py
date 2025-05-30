from collections import deque

def math_operations(*args, a, s, d, m):
    operators = {'a': a, 's': s, 'd': d, 'm': m}
    keys = deque(['a', 's', 'd', 'm'])

    for el in args:
        current_key = keys[0]
        if current_key == 'a':
            operators['a'] += el
        elif current_key == 's':
            operators['s'] -= el
        elif current_key == 'd':
            if el != 0:
                operators['d'] /= el
        elif current_key == 'm':
            operators['m'] *= el
        keys.rotate(-1)
    result = ''
    rounded_result = {key: round(value, 1) for key, value in operators.items()}
    rounded_result = dict(sorted(rounded_result.items(), key=lambda kvp: (-kvp[1], kvp[0])))
    for key, value in rounded_result.items():
        result += f"{key}: {float(value)}\n"
    return result


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))