# Centuries to Minutes
#
# Write a program that reads an integer number of centuries and converts it to years, days, hours, and minutes.

centuries = int(input())
years = centuries * 100
days = int(years * 365.2422)
hours = days * 24
mins = hours * 60
print(f'{int(centuries)} centuries = {int(years)} years = {int(days)} days = {int(hours)} hours = {int(mins)} minutes')