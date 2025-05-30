class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    x = int(input())
    if x < 0:
        raise ValueCannotBeNegative