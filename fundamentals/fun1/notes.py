num1, num2, num3 = input(), input(),input()
print(max(num1, num2, num3))
#max

word = input()
print(word[::-1]) #slice notation
for i in range(len(word) -1, -1, -1):
    print(word[i], end='')
#reverse

n = int(input())
for _ in range(n):
    number = int(input())
    if number % 2 != 0:
        print(f'{number} is odd!')
        break
else:
    print('All numbers are even.')
#for + else ( ako ne vlezem v break > else)


n = int(input())
for i in range(1, n + 1):
    print('*' * i)
for k in range(n -1, 0, -1):
    print('*' * k)
#shapes