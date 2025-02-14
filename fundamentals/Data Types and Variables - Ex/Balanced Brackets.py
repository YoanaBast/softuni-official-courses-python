# 4. Balanced Brackets
#
# On the first line, you will receive n – the number of lines, which will follow.
# On the following n lines, you will receive one of the following:
#
# · Opening bracket – "(",
#
# · Closing bracket – ")" or
#
# · Random string
#
# Your task is to find out if the brackets are balanced.
# That means after every opening bracket should follow a closing one.
# Nested parentheses are not valid, and if, for example, two consecutive opening brackets exist, the expression should be marked as unbalanced.
# You should print "BALANCED" if the parentheses are balanced and "UNBALANCED" otherwise.
left = 0
right = 0
is_balanced = True
current = 0

n = int(input())
for times in range(n):
    command = input()

    if command == '(':
        if current == 1:
            is_balanced = False
        left += 1
        current = 1
    elif command == ')':
        if current == 2 or current == 0:
            is_balanced = False
        right += 1
        current = 2

if left == right and is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')
