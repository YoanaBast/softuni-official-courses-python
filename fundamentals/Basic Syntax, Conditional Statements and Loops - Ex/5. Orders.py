n_orders = int(input())
total = 0
for n in range(n_orders):
    ppc = float(input())
    days = int(input())
    cnpd = int(input())
    if 0.01 <= ppc <= 100.00 \
        and 1 <= days <= 31 \
        and 1 <= cnpd <= 2000:
        price = ppc * days * cnpd
        total += price
        print(f"The price for the coffee is: ${price:.2f}")
        continue
    else:
        continue
print(f'Total: ${total:.2f}')
