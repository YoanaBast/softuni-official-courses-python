n = int(input())
sum = 0
while sum < n:
    new_n = int(input())
    sum += new_n
    if sum >= n:
        print(sum)

