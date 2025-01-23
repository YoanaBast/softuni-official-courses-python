m2_price = 7.61
m2_order = float(input())
total = m2_order * m2_price
discount = total * 0.18
final = total - discount

print(f"The final price is: {final} lv.")
print(f"The discount is: {discount} lv.")
