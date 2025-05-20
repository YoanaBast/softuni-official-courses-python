from collections import deque

color_str = deque(input().split())
main = ["red", "yellow", "blue"]
secondary = {
        "orange": ["red", "yellow"],
        "purple": ["red", "blue"],
        "green": ["yellow", "blue"]
}

collected = []

while color_str:
    first_str = color_str.popleft()
    second_str = color_str.pop() if color_str else ''

    for color in (first_str + second_str, second_str + first_str):
        if color in main or color in secondary:
            collected.append(color)
            break
    else:
        if len(first_str) > 1:
            color_str.insert(len(color_str) // 2, first_str[:-1])

            """ D.insert(index, object) - - insert object before index"""
        if len(second_str) > 1:
            color_str.insert(len(color_str) // 2, second_str[:-1])


for color in collected:
    if color in secondary:
        for el in secondary[color]:
            if el not in collected:
                collected.remove(color)
                break


print(collected)