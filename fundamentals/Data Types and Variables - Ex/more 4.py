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
opening = 0
closing = 0
order = 0
first_check = True
second_check = True
third_check = True
command = ''
last_command = ''
n = int(input())
for i in range(n):
    last_command = command
    command = input()
    order += 1
    if last_command == command:
        first_check = False

    if command == '(':
        opening += 1

    elif command == ')':
        closing += 1

if opening != closing:
    third_check = False

if (first_check == True) and (second_check == True) and (third_check == True):
    print('BALANCED')
else:
    print('UNBALANCED')
