import unittest
from .bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 100)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-50)

    def test_withdraw(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.get_balance(), 70)

    def test_withdraw_negative(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-30)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(150)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 100)


if __name__ == "__main__":
    unittest.main()
