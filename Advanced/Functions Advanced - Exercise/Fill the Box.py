from collections import deque

def fill_the_box(h, l, w, *args):
    volume_box = h * w * l
    args = deque(args)
    while args:
        something = args.popleft()
        if something == 'Finish':
            return f"There is free space in the box. You could put {volume_box} more cubes."

        if isinstance(something, int):
            if volume_box - something <= 0:
                leftover = something - volume_box
                args.appendleft(leftover)
                cubes_left = sum([x for x in args if isinstance(x, int)])
                return f"No more free space! You have {cubes_left} more cubes."

            volume_box -= something




print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))