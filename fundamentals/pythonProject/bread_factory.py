current_energy = 100
current_coins = 100
working_day = input().split('|')
loop_broken = False

for part_of_the_day in working_day:
    command, number = part_of_the_day.split('-')

#REST
    if command == 'rest':
        event, energy_gained = part_of_the_day.split('-')
        energy_gained = int(energy_gained)

        if current_energy == 100:
            energy_gained = 0
        elif  current_energy + energy_gained <= 100:
            current_energy += energy_gained
        else: #cur eng != 100 and cur + gained > 100:
            energy_gained = 100 - current_energy
            current_energy = 100
        print(f"You gained {energy_gained} energy.")
        print(f'Current energy: {current_energy}.')

#ORDER
    elif command == 'order':
        event, coins_gained = part_of_the_day.split('-')
        coins_gained = int(coins_gained)

        if current_energy >= 30:
            current_coins += coins_gained
            print(f'You earned {coins_gained} coins.')
            current_energy -= 30
        else:
            current_energy += 50
            print("You had to rest!")
#INGREDIENT
    else:
        ingredient, coins_spent = part_of_the_day.split('-')
        coins_spent = int(coins_spent)

        if current_coins >= coins_spent:
            current_coins -= coins_spent
            print(f"You bought {ingredient}.")
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            loop_broken = True
            break

if loop_broken == False:
    print("Day completed!")
    print(f"Coins: {current_coins}")
    print(f"Energy: {current_energy}")