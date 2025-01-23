N1 = int(input())
N2 = int(input())
operator = input()

if operator == "+":
    if (N1 + N2) % 2 == 0:
        print(f"{N1} {operator} {N2} = {N1 + N2} - even")
    elif (N1 + N2) % 2 == 1:
        print(f"{N1} {operator} {N2} = {N1 + N2} - odd")

elif operator == "-":
    if (N1 - N2) % 2 == 0:
        print(f"{N1} {operator} {N2} = {N1 - N2} - even")
    elif (N1 - N2) % 2 == 1:
        print(f"{N1} {operator} {N2} = {N1 - N2} - odd")

elif operator == "*":
    if (N1 * N2) % 2 == 0:
        print(f"{N1} {operator} {N2} = {N1 * N2} - even")
    elif (N1 * N2) % 2 == 1:
        print(f"{N1} {operator} {N2} = {N1 * N2} - odd")

elif operator == "/":
    if N2 != 0:
        print(f"{N1} / {N2} = {(N1 / N2):.2f}")
    else:
        print(f"Cannot divide {N1} by zero")

elif operator == "%":
    if N2 != 0:
        print(f"{N1} % {N2} = {N1%N2}")
    else:
        print(f"Cannot divide {N1} by zero")