from collections import deque
from math import floor

start = deque(input().split())
colors = {"main": ["red", "yellow", "blue"],
          "secondary": ["orange", "purple", "green"]}

keepsake = {}
color_maybe = {}
order = 0

while start:
    if len(start) == 1:
        test = start[0]
        if len(test) == 1:
            break
        test_r = 0
    else:
        test = start[0] + start[-1]
        test_r = start[-1] + start[0]


    if test in colors["main"]:
        if test not in keepsake:
            order += 1
            keepsake[test] = order
        if len(start) == 1:
            start.pop()
            continue
        start.pop()
        start.popleft()
        continue

    elif test in colors["secondary"]:
        if test not in color_maybe:
            order += 1
            color_maybe[test] = order
        if len(start) == 1:
            start.pop()
            continue
        start.pop()
        start.popleft()
        continue

    elif test_r in colors["main"]:
        if test_r not in keepsake:
            order += 1
            keepsake[test_r] = order
        if len(start) == 1:
            start.pop()
            continue
        start.pop()
        start.popleft()
        continue

    elif test_r in colors["secondary"]:
        if test_r not in color_maybe:
            order += 1
            color_maybe[test_r] = order
            if len(start) == 1:
                start.pop()
                continue
        start.pop()
        start.popleft()
        continue

    else:
        start[0] = start[0][:-1]
        start[-1] = start[-1][:-1]
        mid = [start[0], start[-1]]

        start = list(start)

        if len(start) % 2 == 0:
            middle = len(start) // 2
        else:
            middle = floor(len(start) / 2)

        left = start[0:middle]
        right = start[middle:]

        start = deque(left + mid + right)
        start.pop()
        start.popleft()

paints = {"orange": ["red", "yellow"],
          "purple": ["red", "blue"],
          "green": ["yellow", "blue"]}

for paint, ordr in color_maybe.items():
    if all(paint in keepsake for paint in paints[paint]):
        keepsake[paint] = ordr

sorted_dict = dict(sorted(keepsake.items(), key=lambda item: item[1]))

print(list(sorted_dict))