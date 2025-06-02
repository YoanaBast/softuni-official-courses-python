class MoneyNotEnoughError(Exception):
    pass
class PINCodeError(Exception):
    pass
class UnderageTransactionError(Exception):
    pass

class MoneyIsNegativeError(Exception):
    pass


stat_pin, balance, age = [int(x) for x in input().split(', ')]
LEGAL_AGE = 18

while True:
    command = input().split('#')
    if command[0] == 'End':
        break

    elif command[0] == 'Send Money':
        money,curr_pin = int(command[1]), int(command[2])
        if money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

        if curr_pin != stat_pin:
            raise PINCodeError("Invalid PIN code")

        if age < LEGAL_AGE:
            raise UnderageTransactionError(f"You must be {LEGAL_AGE} years or older to perform online")

        print(f"Successfully sent {money} money to a friend")
        print(f"There is {(balance - money):.2f} money left in the bank account")

    elif command[0] == 'Receive Money':
        money = int(command[1])
        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        print(f"{(money / 2):.2f} money went straight into the bank account")