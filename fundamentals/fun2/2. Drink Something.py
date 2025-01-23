# Kids drink toddy, teens drink coke, young adults drink beer, and adults drink whisky.
# Create a program that receives a person's age and prints what he/she drinks.
#
# Rules:
age = int(input())
# A kid is defined as someone under or at the age of 14.
is_kid = age <= 14
# A teen is defined as someone under or at the age of 18.
is_teen = 14 < age <= 18
# A young adult is defined as someone under or at the age of 21.
is_young_adult = 18 < age <= 21
# An adult is defined as someone above the age of 21.
is_adult = 21 < age
# Note: All the values are inclusive except the last one!

if is_kid == True:
    drink = 'toddy'
    print(f'drink {drink}')
elif is_teen == True:
    drink = 'coke'
    print(f'drink {drink}')
elif is_young_adult == True:
    drink = 'beer'
    print(f'drink {drink}')
elif is_adult == True:
    drink = 'whisky'
    print(f'drink {drink}')