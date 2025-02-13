electrons_n = int(input())
shell_position = 0
shells = []

while True:
    shell_position += 1
    max_shell = 2 * shell_position ** 2
    if electrons_n < max_shell:
        shells.append(electrons_n)
        electrons_n -= electrons_n
    else:
        shells.append(max_shell)
        electrons_n -= max_shell
    if electrons_n == 0:
        break

print(shells)

