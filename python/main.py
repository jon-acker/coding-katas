from bank_account import Account
from formatter import Formatter

formatter = Formatter()

account = Account(formatter)
account.deposit(1000)
account.deposit(1000)
account.withdraw(500)

output = account.format_statement()

print(output)
