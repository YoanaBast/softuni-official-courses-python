letters = input()
index = []
for indx in range(len(letters)):
    if letters[indx].isupper():
        index.append(indx)

print(index)