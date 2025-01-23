while True:
    destination = input()
    if destination == 'End':
        break

    budget = float(input())
    money = 0.00
    while money < budget:
        nova_sumichka = float(input())
        money += nova_sumichka
    print(f"Going to {destination}!")