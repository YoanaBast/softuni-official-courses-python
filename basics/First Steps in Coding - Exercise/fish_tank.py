length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent_taken = float(input())
# v = a * b * c
# 1 lit = 1000cm (cm3)
total_lit = length_cm * width_cm * height_cm / 1000
free_lit = total_lit - total_lit * percent_taken / 100
print(free_lit)