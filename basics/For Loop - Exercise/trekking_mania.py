group_n = int(input())
Musala, Monblan,Kilimandjaro, K2, Everest = 0, 0, 0, 0, 0
total_people = 0

for _ in range(group_n):
    people_n = int(input())
    if people_n <= 5:
        Musala += people_n
        total_people += people_n
    elif 6 <= people_n <= 12:
        Monblan += people_n
        total_people += people_n
    elif 13 <= people_n <= 25:
        Kilimandjaro += people_n
        total_people += people_n
    elif 26 <= people_n <= 40:
        K2 += people_n
        total_people += people_n
    elif people_n >= 41:
        Everest += people_n
        total_people += people_n


musala_per = (Musala / total_people) * 100
monblan_per = (Monblan / total_people) * 100
kili_per = (Kilimandjaro / total_people) * 100
k2_per = (K2 / total_people) * 100
everest_per = (Everest / total_people) * 100


print(f'{musala_per:.2f}%')
print(f'{monblan_per:.2f}%')
print(f'{kili_per:.2f}%')
print(f'{k2_per:.2f}%')
print(f'{everest_per:.2f}%')