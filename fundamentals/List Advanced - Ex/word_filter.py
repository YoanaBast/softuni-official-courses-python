words = input().split(' ')
filtered_words = [item for item in words if len(item) % 2 == 0]
print(*filtered_words, sep='\n')