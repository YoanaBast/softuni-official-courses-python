start = int(input())
stop = int(input())
magic_n = int(input())
counter = 0
found = False

for num_1 in range(start, stop+1):
    for num_2 in range(start, stop + 1):
        counter += 1
        if num_1 + num_2 == magic_n:
            found = True
            break
    if found:
        break

if not found:
    print(f"{counter} combinations - neither equals {magic_n}")
elif found:
    print(f"Combination N:{counter} ({num_1} + {num_2} = {magic_n})")

