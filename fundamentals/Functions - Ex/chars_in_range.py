# Write a function that receives two characters and returns a single string with all the characters in between them
# (according to the ASCII code), separated by a single space. Print the result on the console
def chars_in_range(uno: str, dos: str) -> str:
    listche = [chr(index) for index in range(first + 1, second)]
    return listche

first = (ord(input()))
second = (ord(input()))

print(*chars_in_range(first, second))