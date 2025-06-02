import regex as re


class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass


emails = []
domains = ('.com', '.bg', '.org', '.net')
name_re = r"[a-zA-Z]{4,}@"


while True:
    email = input()
    if email == 'End':
        break

    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if not re.match(name_re, email): #  match object / None
        raise NameTooShortError("Name must be more than 4 characters")

    if not email.endswith(domains): #  .endswith() can take str or a tuple of str and will auto iterate
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")


    print("Email is valid")