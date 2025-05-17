nums = [float(x) for x in input().split()]
passed = []
for num in nums:
    if num not in passed:
        c = nums.count(num)
        passed.append(num)
        print(f'{num} - {c} times')