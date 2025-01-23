# Write a program that reads a floating-point number and:
# - prints "zero" if the number is zero
# - prints "positive" or "negative"
# - adds "small" if the absolute value of the number is less than 1 and it is not 0, or "large" if it exceeds 1 000 000

n = float(input())
if n < 0:
    if abs(n) < 1 and abs(n) != 0:
        print('small negative')
    elif abs(n) > 1_000_000:
        print('large negative')
    else:
        print('negative')

elif n == 0:
    print('zero')

elif n > 0:
    if abs(n) < 1 and abs(n) != 0:
        print('small positive')
    elif abs(n) > 1_000_000:
        print('large positive')
    else:
        print('positive')