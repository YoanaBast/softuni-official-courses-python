from collections import deque

nums = deque([int(x) for x in input().split()])
tar = int(input())

while len(nums) > 1:
    y = nums.pop()
    if y > tar:
        y = nums.pop()
    for _ in range(len(nums)):
        if y + nums[-1] == tar:
            print(f'{y} + {nums[-1]} = {tar}')
            nums.pop()
            break
        else:
            nums.rotate(-1)

# nums = list(map(int, input().split()))
# tar = int(input())
#
# seen = set()
# for x in nums:
#     complement = tar - x
#     if complement in seen:
#         print(f'{x} + {complement} = {tar}')
#         break
#     seen.add(x)
