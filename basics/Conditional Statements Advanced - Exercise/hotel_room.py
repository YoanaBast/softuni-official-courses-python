month = input()
broi_noshtuvki = int(input())
studio_1_nosht = 0
apaart_1_nosht = 0

# Май и октомври
if month in ('May', 'October') and broi_noshtuvki <= 7:
    studio_1_nosht = 50
    apaart_1_nosht = 65

# За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
elif month in ('May', 'October') and 7 < broi_noshtuvki <= 14:
    studio_1_nosht = 50 * 0.95
    apaart_1_nosht = 65

# За студио, при повече от 14 нощувки през май и октомври : 30% намаление
# За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.
elif month in ('May', 'October') and broi_noshtuvki > 14:
    studio_1_nosht = 50 * 0.70
    apaart_1_nosht = 65 * 0.90

# Юни и септември
elif month in ('June', 'September') and broi_noshtuvki <= 14:
    studio_1_nosht = 75.20
    apaart_1_nosht = 68.70

# За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
# За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.
elif month in ('June', 'September') and broi_noshtuvki > 14:
    studio_1_nosht = 75.20 * 0.80
    apaart_1_nosht = 68.70 * 0.90

# Юли и август
elif month in ('July', 'August') and broi_noshtuvki <= 14:
    studio_1_nosht = 76
    apaart_1_nosht = 77

# За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намалени
elif month in ('July', 'August') and broi_noshtuvki > 14:
    studio_1_nosht = 76
    apaart_1_nosht = 77 * 0.90

studio_full = studio_1_nosht * broi_noshtuvki
apart_full = apaart_1_nosht * broi_noshtuvki

print(f"Apartment: {apart_full:.2f} lv.")
print(f"Studio: {studio_full:.2f} lv.")

# Цената за целия престой да е форматирана с точност до два знака след десетичната запетая.
