from datetime import datetime

class Formatter:
    def __init__(self):
        self.header = "Date | Amount | Balance"

    def format(self, transactions: [int, int, datetime]) -> str:
        format_statement_string = f"{self.header}"

        if not transactions:
            return self.header

        for i in range(len(transactions)):
            date = transactions[i][2].strftime("%Y-%m-%d")
            format_statement_string = f"{format_statement_string}\n{date} | {transactions[i][0]} | {transactions[i][1]}"

        return format_statement_string
