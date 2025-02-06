# Write a function that checks if a given password is valid. Password validations are:
# · It should be 6 - 10 (inclusive) characters long
# · It should consist only of letters and digits
# · It should have at least 2 digits
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
# · "Password must be between 6 and 10 characters"
# · "Password must consist only of letters and digits"
# · "Password must have at least 2 digits

def is_valid(password: str) -> bool:
#LENGHT
    is_good_lenght = len(password) in range(6, 10 + 1)

#NUMS AND DIGS
    for char in password:
        if ord(char) in range(48, 57 +1) or ord(char) in range(65, 90 +1) or ord(char) in range(97, 122+1):
            is_letters_and_digits = True
        else:
            is_letters_and_digits = False
            break
# 2 DIGITS
    nums = 0
    for char in password:
        if ord(char)in range(48, 57 +1):
            nums += 1
        if nums >= 2:
            is_2_or_more_nums = True
        else:
            is_2_or_more_nums = False
# IS IT VALID
    if  is_good_lenght == True and is_letters_and_digits == True and is_2_or_more_nums == True:
        is_password_valid = True
    else:
        is_password_valid = False

    return is_good_lenght, is_letters_and_digits, is_2_or_more_nums, is_password_valid

passwordka = input()

is_good_length, is_letters_and_digits, is_2_or_more_nums, is_password_valid = is_valid(passwordka)
#tuple unpack

if is_password_valid:
    print('Password is valid')
if not is_good_length:
    print('Password must be between 6 and 10 characters')
if not is_letters_and_digits:
    print('Password must consist only of letters and digits')
if not is_2_or_more_nums:
    print('Password must have at least 2 digits')
