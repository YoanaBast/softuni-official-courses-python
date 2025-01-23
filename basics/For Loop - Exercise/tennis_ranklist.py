turniri = int(input())
points = int(input())
W = 2000
F = 1200
SF = 720
new_points = 0
won_turniri = 0
for i in range(1, turniri +1):
    result = input()
    if result == "W":
        won_turniri += 1
        new_points += W
    elif result == "F":
        new_points += F
    elif result == "SF":
        new_points += SF

total_points = points + new_points
print(f"Final points: {total_points}")
print(f"Average points: {int(new_points / turniri)}")
print(f"{((won_turniri / turniri) * 100):.2f}%")


