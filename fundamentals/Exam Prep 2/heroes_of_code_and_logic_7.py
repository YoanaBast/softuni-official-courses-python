heroes_n = int(input())
champ_select = {}

for _ in range(heroes_n):
    hero, HP, MP = input().split()  # "{hero name} {HP} {MP}
    if int(HP) <= 100 and int(MP) <= 200:
        champ_select[hero] = [int(HP), int(MP)]

command = input().split(' - ')
while True:
    if command[0] == 'End':
        break

    elif command[0] == 'CastSpell':
        hero, MP_needed, spell = command[1], command[2], command[3]
        MP = champ_select[hero][1]
        if MP >= int(MP_needed):
            MP -= int(MP_needed)
            champ_select[hero][1] = MP
            print(f"{hero} has successfully cast {spell} and now has {MP} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell}!")

    elif command[0] == 'TakeDamage':
        hero, damage, attacker = command[1], command[2], command[3]
        HP = champ_select[hero][0]
        HP -= int(damage)
        if HP > 0:
            champ_select[hero][0] = HP
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {HP} HP left!")
        else:
            champ_select.pop(hero)
            print(f"{hero} has been killed by {attacker}!")

    elif command[0] == 'Recharge':
        hero, amount = command[1], command[2]
        MP = champ_select[hero][1]
        if MP + int(amount) > 200:
            amount = 200 - MP
            MP = 200
        else:
            MP += int(amount)
        champ_select[hero][1] = MP
        print(f"{hero} recharged for {amount} MP!")

    elif command[0] == 'Heal':
        hero, amount = command[1], command[2]
        HP = champ_select[hero][0]
        if HP + int(amount) > 100:
            amount = 100 - HP
            HP = 100
        else:
            HP += int(amount)
        champ_select[hero][0] = HP
        print(f"{hero} healed for {amount} HP!")

    command = input().split(' - ')

for hero in champ_select.keys():
    print(hero)
    print(f'  HP: {champ_select[hero][0]}\n  MP: {champ_select[hero][1]}')
