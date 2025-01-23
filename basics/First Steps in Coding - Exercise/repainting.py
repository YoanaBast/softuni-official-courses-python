sheet_price = 1.50
paint_price = 14.50
razr_price = 5.00

sheet_count = int(input())
paint_count = int(input())
razr_count = int(input())
hours = int(input())

materials = ((sheet_count + 2) * sheet_price) + ((paint_count + paint_count * 0.10) * paint_price) + \
            (razr_count * razr_price) + 0.40
hourly_pay = 0.30 * materials
total_pay = hours * hourly_pay
total_expenses = materials + total_pay
print(total_expenses)
