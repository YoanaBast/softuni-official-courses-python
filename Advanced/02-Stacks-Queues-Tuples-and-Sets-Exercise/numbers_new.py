first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())
n = int(input())

for _ in range(n):
    command = input()
    if command.startswith('Add First'):
        numbers = [int(x) for x in command.split() if x.isdigit()]
        for digi in numbers:
                first.add(digi)

    elif command.startswith('Add Second'):
        numbers = [int(x) for x in command.split() if x.isdigit()]
        for digi in numbers:
                second.add(digi)

    elif command.startswith('Remove First'):
        numbers = [int(x) for x in command.split() if x.isdigit()]
        for digi in numbers:
            if digi in first:
                first.remove(digi)

    elif command.startswith('Remove Second'):
        numbers = [int(x) for x in command.split() if x.isdigit()]
        for digi in numbers:
            if digi in second:
                second.remove(digi)

    elif command == 'Check Subset':
        if first < second  or first > second:
            print('True')
        else:
            print('False')

first_s = map(str, sorted(first))
second_s = map(str, sorted(second))

print(', '.join(first_s))
print(', '.join(second_s))