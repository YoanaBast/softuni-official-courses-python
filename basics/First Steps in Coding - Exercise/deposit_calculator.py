deposit = float(input())
srok = int(input())
lihva = float(input())
lihva_procent = lihva / 100
sum = deposit + srok * ((deposit * lihva_procent) / 12)
print(sum)
