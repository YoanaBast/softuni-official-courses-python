n = int(input())
redica = 1
print(redica)

while redica < n:
    nova_redica = ((redica * 2) + 1)
    redica = nova_redica
    print(redica)
    if redica > n - nova_redica:
        break


