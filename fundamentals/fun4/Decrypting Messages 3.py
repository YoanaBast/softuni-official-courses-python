# 3. Decrypting Messages
#
# On the first line, you will receive a key (integer).
# On the second line, you will receive n – the number of lines, which will follow. On the next n lines –
# you will receive a lower and an uppercase letter per line.
#
# You should add the key to each of the characters and append them to a message. In the end, print the decrypted message.
smol_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
big_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
key = int(input())
n = int(input())
result = ''
for i in range(n):
    let1 = input()
    if let1 in smol_list:
        let1_value = smol_list.index(let1)
        let1_value_new = smol_list.index(let1) + key
        new_let1 = smol_list[let1_value_new]
        result += new_let1

    else:
        let1_value = big_list.index(let1)
        let1_value_new = big_list.index(let1) + key
        new_let1 = big_list[let1_value_new]
        result += new_let1
print(result)


