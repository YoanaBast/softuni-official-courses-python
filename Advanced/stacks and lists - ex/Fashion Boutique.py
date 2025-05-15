
clothes_stack = [int(x) for x in input().split()]
r_capacity = int(input())
current_rack = 0
total_racks = 1

while clothes_stack:
    if current_rack + clothes_stack[-1] <= r_capacity:
        current_rack += clothes_stack[-1]
        clothes_stack.pop()
    else:
        current_rack = 0
        total_racks += 1
        current_rack += clothes_stack[-1]
        clothes_stack.pop()

print(total_racks)
