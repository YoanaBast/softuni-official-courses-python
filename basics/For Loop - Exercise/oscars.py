actor_name = input()
academy_points = float(input())
appraisers_n = int(input())

for _ in range(1, appraisers_n +1):
    appraiser_name = input()
    appraiser_points = float(input())
    academy_points += (len(appraiser_name) * appraiser_points) / 2
    if academy_points > 1250.5:
        break

if academy_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {(academy_points):.1f}!")
elif academy_points < 1250.5:
    print(f"Sorry, {actor_name} you need {(1250.5 - academy_points):.1f} more!")

