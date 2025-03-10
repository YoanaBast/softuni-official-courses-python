while True:
    string = input()
    if string == 'end':
        break
    reversed = string[::-1]
    print(f"{string} = {reversed}")