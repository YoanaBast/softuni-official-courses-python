first = set(input().split())
second = set(input().split())
n = int(input())

for _ in range(n):
    command = input()
    if command.startswith('Add First'):
        for digi in command:
            if digi.isdigit():
                first.add(digi)

    elif command.startswith('Add Second'):
        for digi in command:
            if digi.isdigit():
                second.add(digi)

    elif command.startswith('Remove First'):
        nums = set()
        for digi in command:
            if digi.isdigit():
                nums.add(digi)
                for num in nums:
                    if num in second:
                        first.remove(num)

    elif command.startswith('Remove Second'):
        nums = set()
        for digi in command:
            if digi.isdigit():
                nums.add(digi)
                for num in nums:
                    if num in second:
                        second.remove(num)


    elif command == 'Check Subset':
        if first < second  or first > second:
            print('True')
        else:
            print('False')

