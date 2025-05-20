first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())
n = int(input())

for _ in range(n):
    command = input()
    numbers = [int(x) for x in command.split() if x.isdigit()]

    if command.startswith('Add First'):
        first.update(numbers)

    elif command.startswith('Add Second'):
        second.update(numbers)

    elif command.startswith('Remove First'):
        first.difference_update(numbers)

    elif command.startswith('Remove Second'):
        second.difference_update(numbers)
        """ Remove all elements of another set from this set. """

    elif command == 'Check Subset':
        print(first.issubset(second) or second.issubset(first))
        """ Report whether another set contains this set. """

first_s = map(str, sorted(first))
second_s = map(str, sorted(second))

print(', '.join(first_s))
print(', '.join(second_s))