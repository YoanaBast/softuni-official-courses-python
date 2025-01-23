first_num = int(input())
second_num = int(input())

# Loop through the range of numbers
for number in range(first_num, second_num + 1):
    number_to_str = str(number)  # Convert the number to a string for digit processing
    even_sum = 0  # Initialize the sum of digits at even indices
    odd_sum = 0   # Initialize the sum of digits at odd indices

    for index, digit in enumerate(number_to_str):  # Enumerate provides both index and digit
        if index % 2 == 0:  # Even index
            even_sum += int(digit)
        else:  # Odd index
            odd_sum += int(digit)

    # Check if the sums of digits at even and odd indices are equal
    if even_sum == odd_sum:
        print(number, end=' ')