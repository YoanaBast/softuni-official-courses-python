movie_budget = float(input())
people_count = int(input())
clothes_price_per_person = float(input())
decor = 0.10 * movie_budget
if people_count > 150:
    clothes_price_per_person = clothes_price_per_person * 0.90

quick_maths = movie_budget - decor - (clothes_price_per_person * people_count)

if quick_maths < 0:
    no_negative = quick_maths * -1
    print("Not enough money!")
    print(f"Wingard needs {no_negative:.2f} leva more.")
elif quick_maths >= 0:
    print("Action!")
    print(f"Wingard starts filming with {quick_maths:.2f} leva left.")
