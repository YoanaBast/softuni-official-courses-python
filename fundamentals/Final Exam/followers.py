usernames = {}
command = input().split(': ')
while True:
    if command[0] == "Log out":
        print(f"{len(usernames)} followers")
        for user in usernames.keys():
            print(f'{user}: {usernames[user][0] + usernames[user][1]}')
        break

    elif command[0] == 'New follower':  # "New follower: {username}":
        username = command[1]
        if username not in usernames.keys():
            usernames[username] = [0, 0] # like, comment

    elif command[0] == 'Like':  # "Like: {username}: {count}":
        username, count = command[1], int(command[2])
        if username not in usernames.keys():
            usernames[username] = [count, 0]
        else:
            usernames[username][0] += count

    elif command[0] == 'Comment':  # "Comment: {username}":
        username = command[1]
        if username not in usernames.keys():
            usernames[username] = [0, 1]
        else:
            usernames[username][1] += 1

    elif command[0] == 'Blocked':  # "Blocked: {username}":
        username = command[1]
        if username not in usernames.keys():
            print(f"{username} doesn't exist.")
        else:
            usernames.pop(username)
    command = input().split(': ')
