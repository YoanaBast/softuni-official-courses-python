words = input().split(' ')
palindr = input()
pali = []
for word in words:
    if word == word[::-1]:
        pali.append(word)

count = pali.count(palindr)
print(pali)
print(f'Found palindrome {count} times')