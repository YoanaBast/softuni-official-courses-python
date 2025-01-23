prime_num_sum, non_prime_bum_sum = 0, 0
command = input()
while command != 'stop':
    current_num = int(command)
    if current_num < 0:
        print("Number is negative.")
        command = input()
        continue
    is_prime = True
    for divisor in range(2, current_num):
        if current_num % divisor == 0:
            is_prime = False
            break

    if is_prime:
        prime_num_sum += current_num
    else:
        non_prime_bum_sum += current_num

    command = input()

print(f"Sum of all prime numbers is: {prime_num_sum}")
print(f"Sum of all non prime numbers is: {non_prime_bum_sum}")
