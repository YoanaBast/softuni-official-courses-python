# You will be given strings until you receive the command "End".
# For each string given, you should print a string in which each character (case-sensitive) is repeated twice.
# Note that if you receive the string "SoftUni", you should NOT print it!
new_word = ''
while True:
    command = input()

    if command == 'End':
        break

    else:
        word = command
        for w in range(len(word)):
            dd = word[w] * 2
            new_word += dd
            if word == 'SoftUni':
                new_word = ''
                continue
            elif w == len(word) - 1:
                print(new_word)
                new_word = ''
        continue


