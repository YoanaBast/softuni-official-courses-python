import re

places = input()

regex = r"([=|/])(?P<place>[A-Z][a-zA-Z]{2,})(\1)"
match_it = re.finditer(regex, places)

places_lst = []
for item in match_it:
    places_lst.append(item.group('place'))

points = 0
for place in places_lst:
    points += len(place)

print(f'Destinations: {", ".join(places_lst)}')
print(f'Travel Points: {points}')