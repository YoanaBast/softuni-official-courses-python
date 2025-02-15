sequence_of_number = input().split()
stringche = list(input())
nums_list = [int(num)for num in sequence_of_number]
message = []

for num in nums_list:
    temp = (sum(list(map(int, str(num)))))  # sum of all digits in num
    if temp < len(stringche):
        index = temp
    else:
        index = temp - len(stringche)
    message.append(stringche[index])
    stringche.pop(index)

print(''.join(message))
