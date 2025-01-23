# Да се напише програма, която изчислява колко пари са дадени за благотворителност и колко е получил
# всеки един член на групата.

# Вход:
# От конзолата се четат 4 реда:
# 1. Брой танцьори – цяло число в интервала [1 … 10]
dancer_count = int(input())
# 2. Брой точки – реално число в интервала [1.00 … 10000.00]
points_count = float(input())
# 3. Сезон – текст със следните възможности - "summer" или "winter"
season = input()
# 4. Място – текст със следните възможности - "Bulgaria" или "Abroad"
place = input()

# След успешно класиране, група заминава за финалното състезание. След представянето си всяка група
# получава парична награда. Тя зависи от: държавата, в която се е провело състезанието; броя точки, които
# журито е дало и сезонът, през който се е провело състезанието.
# • Ако състезанието се е провело в България паричната награда се изчислява като се умножат точките
# по броя участниците.
# От получената сума се изваждат разходите посочени в проценти спрямо сезона, през който се е провел:
if place == 'Bulgaria':
    money_prize = points_count * dancer_count
    if season == 'summer':
        money_after_expenses = money_prize - (money_prize * 0.05)
    elif season == 'winter':
        money_after_expenses = money_prize - (money_prize * 0.08)
    # • Ако се е провело в чужбина – се умножават броя участници по броя точки и към тях се добавя 50% от
# получената сума.
elif place == 'Abroad':
    money_prize = (dancer_count * points_count) + ((dancer_count * points_count) / 2)
    if season == 'summer':
        money_after_expenses = money_prize - (money_prize * 0.10)
    elif season == 'winter':
        money_after_expenses = money_prize - (money_prize * 0.15)

# След завръщането си групата дарява 75% от сумата, след приспаднатите разходи, за благотворителност.
final_money = money_after_expenses * 0.25
charity = money_after_expenses * 0.75
# Останалата сума се разпределя между членовете на групата.
money_per_dancer = final_money / dancer_count

# Изход:
# На конзолата се отпечатват 2 реда:
# • Сумата, която са дали за благотворителност
print(f"Charity - {charity:.2f}")
# • Сумата, която е получил всеки танцьор
print(f"Money per dancer - {money_per_dancer:.2f}")
# Сумите да бъдат форматирани до втория знак след десетичната запетая.