# 5. Print Part of the ASCII Table
#
# Write a program that prints part of the ASCII table characters on the console, separated by a single space.
# On the first line of input, you will receive the char index you should start with.
# On the second line - the index of the last character you should print.

start = int(input())
last = int(input())

for index in range(start, last +1):
    print(chr(index), end = ' ')