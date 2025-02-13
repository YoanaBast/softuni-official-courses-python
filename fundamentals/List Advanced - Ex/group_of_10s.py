nums = list(map(int, input().split(', ')))
counter = 10
while nums:
    groups = [item for item in nums if item <= counter]
    nums = list(filter(lambda x: x not in groups, nums))
    print(f"Group of {counter}'s: {groups}")
    counter += 10