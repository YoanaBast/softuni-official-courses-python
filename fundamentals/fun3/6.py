# Next Happy Year
#
# You are saying goodbye to your best friend: "See you next happy year".
# Happy Year is the year with only distinct digits, for example, 2018.
# Write a program that receives an integer number and finds the next happy year.

year = int(input())

while True:
    year += 1
    year_str = str(year)

    if len(set(year_str)) == len(year_str):
        break

print(year)
