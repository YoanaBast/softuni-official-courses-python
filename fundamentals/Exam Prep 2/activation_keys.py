raw_key = input()  # letters and numbers only

command = input().split('>>>')
while True:
    if command[0] == 'Generate':
        print(f"Your activation key is: {raw_key}")
        break

    elif command[0] == 'Contains':
        substring = command[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")

    elif command[0] == 'Flip':
        up_low, start_indx, end_indx = command[1], int(command[2]), int(command[3])
        if start_indx < len(raw_key) and end_indx < len(raw_key):
            substring = raw_key[start_indx:end_indx]
            if up_low == 'Upper':
                substring = substring.upper()
                raw_key = raw_key[:start_indx] + substring + raw_key[end_indx:]
                print(raw_key)
            elif up_low == 'Lower':
                substring = substring.lower()
                raw_key = raw_key[:start_indx] + substring + raw_key[end_indx:]
                print(raw_key)

    elif command[0] == 'Slice':
        start_indx, end_indx = int(command[1]), int(command[2])
        if start_indx < len(raw_key) and end_indx < len(raw_key):
            substring = ''
            raw_key = raw_key[:start_indx] + substring + raw_key[end_indx:]
            print(raw_key)

    command = input().split('>>>')