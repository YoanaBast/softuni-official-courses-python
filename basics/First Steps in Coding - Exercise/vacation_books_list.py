pages = int(input())
page_per_hour = int(input())
days = int(input())
hours_needed = pages // page_per_hour / days
print(int(hours_needed))