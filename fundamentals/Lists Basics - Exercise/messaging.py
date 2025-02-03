sequence_of_number = input().split()
stringche = list(input())
nums_list = []
message = []

for num in sequence_of_number:
    nums_list.append(int(num))

for command in nums_list:
    total = 0
    while command > 0:
        digit = command % 10  # Extract last digit
        total += digit  # Add to sum
        command //= 10  # Remove last digit
        index = total // 10
        message.append(stringche[index])
        stringche.pop(index)
        continue

print(index)
print(stringche)
print(message)

