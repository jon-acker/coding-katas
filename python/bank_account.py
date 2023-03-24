from datetime import datetime

from formatter import Formatter

class Account:

    def __init__(self, clock: datetime):
        self.clock = clock

        self.transactions: [int, int, datetime] = []

        self.balance_total: int = 0

    def format_statement(self) -> str:

        return Formatter().format(self.transactions)

    def deposit(self, amount: int):
        self.balance_total += amount

        """   def format_time(time_to_format: datetime) -> str:
                s = time_to_format.strftime('%Y-%m-%d %H:%M:%S%f')
                return s[:-6]"""

        statement_line = (amount, self.balance_total, self.clock.now())

        self.transactions.append(statement_line)

    def withdraw(self, amount: int):
        self.balance_total -= amount

        statement_line = (amount, self.balance_total, self.clock.now())

        self.transactions.append(statement_line)
