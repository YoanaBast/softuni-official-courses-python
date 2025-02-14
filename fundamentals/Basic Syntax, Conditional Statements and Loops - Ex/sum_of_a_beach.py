strigngche = input()
strigngche = strigngche.lower()
keywords = ['sand', 'water', 'fish', 'sun']
counter = 0
for key in keywords:
    if key in strigngche:
        counter += strigngche.count(key)
print(counter)