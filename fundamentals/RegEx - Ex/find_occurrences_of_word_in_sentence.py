import re

stirng = input()
word = input()
regex = rf"\b{word}\b"
result = re.findall(regex, stirng, re.IGNORECASE)
print(len(result))