# 6. Triples of Latin Letters
#
# Write a program to read an integer N
# and print all triples of the first N small Latin letters, ordered alphabetically:
n = int(input())

for i1 in range(97, 97 + n):
    for i2 in range(97, 97 + n):
        for i3 in range(97, 97 + n):
            print(chr(i1)+chr(i2)+chr(i3))
