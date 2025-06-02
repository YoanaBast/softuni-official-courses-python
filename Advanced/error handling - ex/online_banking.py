class MoneyNotEnoughError(Exception):
    pass
class PINCodeError(Exception):
    pass
class UnderageTransactionError(Exception):
    pass

class MoneyIsNegativeError(Exception):
    pass


stat_pin, balance, age = input().split(', ')
LEGAL_AGE = 18

while True:
    command = input().split()
    if command[0] == 'End':
        break

    elif command[0] == 'Send':
        _, money, curr_pin = command[1].split('#')
        if int(money) > int(balance):
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

        if curr_pin != stat_pin:
            raise PINCodeError("Invalid PIN code")

        if int(age) < LEGAL_AGE:
            raise UnderageTransactionError(f"You must be {LEGAL_AGE} years or older to perform online")

        print(f"Successfully sent {money} money to a friend")
        print(f"There is {(int(balance) - int(money)):.2f} money left in the bank account")

    elif command[0] == 'Receive':
        _, money = command[1].split('#')
        if int(money) < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        print(f"{(int(money) / 2):.2f} money went straight into the bank account")