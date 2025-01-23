# ex_cost = float(input())
# available_money = float(input())
# spend_day = 0
# save_day = 0
#
#
# while True:
#     action_type = input()  # spend; save
#     sumichka = float(input())
#
#     if action_type == 'spend':
#         available_money -= sumichka
#         spend_day += 1
#         if spend_day > 4:
#             break
#         if sumichka > available_money:
#             available_money = 0
#
#     elif action_type == 'save':
#         available_money += sumichka
#         save_day += 1
#         if available_money >= ex_cost:
#             break
#
#
#
# if spend_day > 4:
#     print(f"You can't save the money.")
#     print(spend_day + save_day)
# elif available_money >= ex_cost:
#     print(f"You saved the money for {spend_day + save_day} days.")

# ex_cost = float(input()) #110
# money = float(input()) #60
# is_still_savnig = (ex_cost > money)
# spend_days, save_days = 0, 0
#
# while is_still_savnig:
#     action = input() # spend, spend
#     amount_ss = float(input()) #10, 10
#
#     if action == 'spend':
#         spend_days +=1 #5
#         if spend_days == 5:
#             break
#         if amount_ss >= money:
#             money = 0
#             continue
#
#         money -= amount_ss #50
#
#     elif action == 'save':
#         money += amount_ss
#         save_days +=1
#         if money == ex_cost:
#             break
#
# total_days = spend_days + save_days
#
# if spend_days == 5:
#     print("You can't save the money.")
#     print(f"{total_days}")
#
# elif money == ex_cost:
#     print(f"You saved the money for {total_days} days.")

needed_money = float(input())
owned_money = float(input())
days_counter = 0
spending_counter = 0

while owned_money < needed_money and spending_counter < 5:
    command = input()
    money = float(input())
    days_counter +=1

    if command == 'save':
        owned_money += money
        spending_counter = 0
    elif command == 'spend':
        owned_money -= money
        spending_counter +=1
        if owned_money < 0:
            owned_money = 0


if spending_counter == 5:
    print("You can't save the money.")
    print(f"{days_counter}")

if owned_money >= needed_money:
    print(f"You saved the money for {days_counter} days.")
