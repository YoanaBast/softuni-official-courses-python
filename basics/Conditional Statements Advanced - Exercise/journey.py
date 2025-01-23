budget = float(input())
season = input() #"summer” или "winter”.
where_sleep = ''
where_go =''
spend = 0
if budget <= 100:
    where_go = 'Bulgaria'
    if season == 'summer':
        spend = 0.30 * budget
    elif season == 'winter':
        spend = 0.70 * budget
elif budget <= 1_000:
    where_go = "Balkans"
    if season == 'summer':
        spend = 0.40 * budget
    elif season == 'winter':
        spend = 0.80 * budget
elif budget > 1_000:
    where_go = "Europe"
    spend = 0.90 * budget

if season == 'summer' and where_go != "Europe":
    where_sleep = 'Camp'
else:
    where_sleep = 'Hotel'
print(f"Somewhere in {where_go}")
print(f"{where_sleep} - {spend:.2f}")
