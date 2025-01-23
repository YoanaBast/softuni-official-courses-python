target = 10_000
steps = 0

command = input()
while command != 'Going home':
    walky_walky = int(command)
    steps += walky_walky

    if steps >= target:
        break

    command = input()

if command == 'Going home':
    extra_walky = int(input())
    steps += extra_walky

if steps >= target:
    print("Goal reached! Good job!")
    print(f"{steps - target} steps over the goal!")
else:
    print(f'{target - steps} more steps to reach goal.')

