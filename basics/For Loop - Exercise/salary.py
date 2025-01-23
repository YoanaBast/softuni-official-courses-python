facebook_fine = 150
instagram_fine = 100
reddit_fine = 50

open_tabs = int(input())
salary = float(input())

for web in range(1, open_tabs +1):
    web_name = input()
    if web_name == "Facebook":
        salary -= facebook_fine
        if salary <= 0:
            break
    if web_name == "Instagram":
        salary -= instagram_fine
        if salary <= 0:
            break
    if web_name == "Reddit":
        salary -= reddit_fine
        if salary <= 0:
            break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(int(salary))


