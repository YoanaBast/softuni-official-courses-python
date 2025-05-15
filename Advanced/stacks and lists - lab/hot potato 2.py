from collections import deque

children = deque(input().split())
potato = int(input())

while len(children) > 1:
    children.rotate(-(potato-1))
    print(f'Removed {children.popleft()}')

print(f'Last is {children[0]}')

# this is with O1 complexity