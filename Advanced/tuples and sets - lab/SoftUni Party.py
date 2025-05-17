n = int(input())
invitations = set()
for _ in range(n):
    invitations.add(input())

while True:
    command = input()
    if command == 'END':
        print(len(invitations))
        s = sorted(invitations)
        for inv in s:
            print(inv)
        break
    if command in invitations:
        invitations.remove(command)