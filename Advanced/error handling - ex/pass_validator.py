import regex as re


class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass

MIN_PWD_LEN =8

while True:
    command = input()
    if command == 'Done':
        break

    if len(command) < MIN_PWD_LEN:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if command.isdigit() or command.isalpha() or re.match(r'^[^a-zA-Z0-9]+$', command):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if re.match(r'^[a-zA-Z0-9]+$', command):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if ' ' in command:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")