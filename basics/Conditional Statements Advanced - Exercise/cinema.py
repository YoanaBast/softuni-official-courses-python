tip_projekciq = input()
r = int(input()) #redove
c = int(input()) #koloni
ticket_price = 0
if tip_projekciq == 'Premiere':
    ticket_price = 12.00

elif tip_projekciq == 'Normal':
    ticket_price = 7.50

elif tip_projekciq == 'Discount':
    ticket_price = 5.00

income = ticket_price * r * c
print(f"{income:.2f} leva")