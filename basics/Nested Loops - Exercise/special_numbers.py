N = int(input("Enter a number (1 to 600000): "))

# Loop through all numbers from 1111 to 9999
special_numbers = []
for number in range(1111, 10000):
    is_special = True
    for digit in str(number):
        digit = int(digit)
        # Skip invalid division (0 as a digit) and check divisibility
        if digit == 0 or N % digit != 0:
            is_special = False
            break
    if is_special:
        special_numbers.append(str(number))

# Print all special numbers separated by space
print(" ".join(special_numbers))