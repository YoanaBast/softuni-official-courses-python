# On the first line, you will receive a single number n.
# On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:
# # · even
# # · odd
# # · negative
# # · positive
# # Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

n = int(input())
nums = []

even = []
is_even = False

odd = []
is_odd = False

positive = []
is_positive = False

negative = []
is_negative = False

for _ in range(n):
    inte = int(input())
    nums.append(inte)

    if inte % 2 == 0:
        even.append(inte)
        is_even = True

    if inte % 2 != 0:
        odd.append(inte)
        is_odd = True

    if inte < 0:
        negative.append(inte)
        is_negative = True

    if inte >= 0:
        positive.append(inte)
        is_positive = True

command = input()

if command == 'even' and is_even:
    print(even)
elif command == 'odd' and is_odd:
    print(odd)
elif command == 'negative' and is_negative:
    print(negative)
elif command == 'positive' and positive:
    print(positive)

