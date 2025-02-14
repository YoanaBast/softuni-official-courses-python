# 3. Decrypting Messages
#
# On the first line, you will receive a key (integer).
# On the second line, you will receive n – the number of lines, which will follow. On the next n lines –
# you will receive a lower and an uppercase letter per line.
#
# You should add the key to each of the characters and append them to a message. In the end, print the decrypted message.

key = int(input())
n = int(input())
result = ''
for i in range(n):
    let1 = input()
    new_let = chr(ord(let1) + key)
    result += new_let
print(result)


