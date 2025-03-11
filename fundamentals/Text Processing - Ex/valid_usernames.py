usernames = input().split(', ')
valid = []
for username in usernames:
    if not (3 <= len(username) <= 16):
        continue
    else:
        is_valid = True
        for char in username:
            if  char.isdigit() or char.isalpha() or char == '-' or char == '_':
                is_valid = True
            else:
                is_valid = False
                break
        if is_valid:
            valid.append(username)
print('\n'.join(valid))