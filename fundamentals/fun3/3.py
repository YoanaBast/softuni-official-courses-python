# 3. Pounds to Dollars
#
# Write a program that converts British pounds (integer) to US dollars formatted to the 3rd decimal point.
#
# 1 British Pound = 1.31 Dollars.

GBP = float(input())
USD = GBP * 1.31
print(f'{USD:.3f}')