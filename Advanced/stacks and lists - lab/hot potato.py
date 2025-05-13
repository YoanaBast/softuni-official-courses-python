from collections import deque

children = deque(input().split())
n = int(input())
counter = 0

while len(children) > 1:
    for child in children:
        counter += 1
        if counter == n:
            print(f'Removed {child}')
            position = children.index(child)
            children.remove(child)
            counter = -position
            # I couldn't figure out a way to loop the children, as the moment someone is removed the for loop breaks;
            # instead I set the counter to negative number of children at the start of the queue (ones that need to be skipped for the round).
            # In reality they are not skipped from the loop but their number is subtracted so the potato is being passed to the next in turn
            break
print(f'Last is {children[0]}')
