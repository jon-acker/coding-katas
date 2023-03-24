import datetime
import unittest
from unittest.mock import MagicMock, Mock

from bank_account import Account


class TestBankAccount(unittest.TestCase):
    def test_statement_has_no_entries_in_initial_state(self):

        account = Account()
        output = account.format_statement()
        self.assertEqual("Date | Amount | Balance", output)

    def test_print_balance_line_after_deposit_of_1000(self):

        account = Account()
        account.deposit(1000)

        # return the amount correctly
        output = account.format_statement()
        expected = "Date | Amount | Balance\n" \
                   "2023-01-10 | 1000 | 1000"
        self.assertEqual(expected, output)

    def test_print_balance_line_after_multiple_deposits_of_1000(self):
        account = Account()
        account.deposit(1000)
        account.deposit(1000)

        # return the amount correctly
        output = account.format_statement()
        expected = "Date | Amount | Balance\n" \
                   "2023-01-10 | 1000 | 1000\n" \
                   "2023-01-10 | 1000 | 2000"
        self.assertEqual(expected, output)

    def test_print_balance_line_after_multiple_deposits_and_withdrawal(self):
        account = Account()
        account.deposit(1000)
        account.withdraw(100)

        # return the amount correctly
        output = account.format_statement()
        expected = "Date | Amount | Balance\n" \
                   "2023-01-10 | 1000 | 1000\n" \
                   "2023-01-10 | 100 | 900"
        self.assertEqual(expected, output)

    def test_print_balance_line_after_multiple_deposits_and_withdrawal_with_different_dates(self):
        clock = Mock()

        # bank account now has a clock that we can control
        account = Account(clock)

        # set current date to 10th
        clock.configure_mock(**{'now.return_value': datetime.datetime(2023, 1, 10)})

        account.deposit(1000)

        # set current date to 11th
        clock.configure_mock(**{'now.return_value': datetime.datetime(2023, 1, 11)})

        account.withdraw(100)

        # return the amount correctly
        output = account.format_statement()


        expected = "Date | Amount | Balance\n" \
                   "2023-01-10 | 1000 | 1000\n" \
                   "2023-01-11 | 100 | 900"
        self.assertEqual(expected, output)

if __name__ == '__main__':
    unittest.main()
