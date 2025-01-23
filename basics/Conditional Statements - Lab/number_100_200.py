# ⦁	под 100 отпечатайте: "Less than 100"
# ⦁	между 100 и 200 отпечатайте: "Between 100 and 200"
# ⦁	над 200 отпечатайте: "Greater than 200"

num = int(input())

if num < 100:
    print("Less than 100")
elif num >= 100 and num <= 200:
    print("Between 100 and 200")
elif num > 200:
    print("Greater than 200")
