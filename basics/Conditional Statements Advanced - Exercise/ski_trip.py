stay_days = int(input())
type_of_stay = input() #"room for one person", "apartment" или "president apartment"
assessment = input() #"positive"  или "negative"

nights = stay_days - 1
room_for_one_person = 18.00
apartment = 25.00
president_apartment = 35.00


if nights < 10:
    room_for_one_person = 18.00
    apartment = 25.00 * 0.70 #-30%
    president_apartment = 35.00 * 0.90 #-10%
elif 10 <= nights <= 15:
    room_for_one_person = 18.00
    apartment = 25.00 * 0.65 #-35%
    president_apartment = 35.00 * 0.85 #-15%
elif nights > 15:
    room_for_one_person = 18.00
    apartment = 25.00 * 0.50 #-50%
    president_apartment = 35.00 * 0.80 #-20%

total_1_room = room_for_one_person * nights
total_apt = apartment * nights
total_president = president_apartment * nights

if assessment == 'positive':
    total_1_room = total_1_room + (total_1_room * 0.25)
    total_apt = total_apt + (total_apt * 0.25)
    total_president = total_president + (total_president * 0.25)
elif assessment == 'negative':
    total_1_room = total_1_room - (total_1_room * 0.10)
    total_apt = total_apt - (total_apt * 0.10)
    total_president = total_president - (total_president * 0.10)

if type_of_stay == "room for one person":
    print(f"{total_1_room:.2f}")
elif type_of_stay == "apartment":
    print(f"{total_apt:.2f}")
elif type_of_stay == "president apartment":
    print(f"{total_president:.2f}")
