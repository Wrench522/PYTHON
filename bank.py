class BankAccount:
    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"KSh {amount} deposited successfully.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient funds. Withdrawal denied.")
        else:
            self.balance -= amount
            print(f"KSh {amount} withdrawn successfully.")

    def display_balance(self):
        print("\n--- Account Details ---")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Balance: KSh {self.balance}")


# 1. Create two customer accounts
account1 = BankAccount("001", "Alice", 5000)
account2 = BankAccount("002", "Bob", 10000)

# 2. Deposit money into each account
account1.deposit(2000)
account2.deposit(3000)

# 3. Perform withdrawals
account1.withdraw(1000)
account2.withdraw(15000)  # should show insufficient funds

# 4. Display final balances
account1.display_balance()
account2.display_balance()