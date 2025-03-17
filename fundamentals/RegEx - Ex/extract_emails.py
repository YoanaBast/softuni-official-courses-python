import re
emails = input()
regex =r"(?<=\s)[A-Zza-z0-9]+[\.\-\_]*[A-Za-z0-9]+@[a-z]+[-]*[a-z]+\.[a-z]+[\.[a-z]+]*\b"
matches = re.findall(regex, emails)
result = '\n'.join(matches)
print(result)