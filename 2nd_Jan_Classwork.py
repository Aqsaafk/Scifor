class BankAccount:
    def __init__(self, initial_balance, pin):
        self.balance = initial_balance
        self.pin = pin

    def withdraw(self, amount, entered_pin):
        if self._validate_pin(entered_pin):
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal successful. Remaining balance: {self.balance}")
            else:
                print("Insufficient balance!")
        else:
            print("Invalid PIN. Withdrawal failed.")

    def deposit(self, amount, entered_pin):
        if self._validate_pin(entered_pin):
            if amount > 0:
                self.balance += amount
                print(f"Deposit successful. New balance: {self.balance}")
            else:
                print("Invalid deposit amount.")
        else:
            print("Invalid PIN. Deposit failed.")

    def check_balance(self, entered_pin):
        if self._validate_pin(entered_pin):
            return self.balance
        else:
            print("Invalid PIN. Cannot check balance.")
            return None

    def _validate_pin(self, entered_pin):
        return entered_pin == self.pin


# Example usage:
initial_balance = float(input("Enter initial balance: "))
pin_number = input("Set your ATM PIN: ")

# Create a BankAccount object
account = BankAccount(initial_balance, pin_number)

# Withdraw money
withdraw_amount = float(input("Enter withdrawal amount: "))
withdraw_pin = input("Enter ATM PIN for withdrawal: ")
account.withdraw(withdraw_amount, withdraw_pin)

# Deposit money
deposit_amount = float(input("Enter deposit amount: "))
deposit_pin = input("Enter ATM PIN for deposit: ")
account.deposit(deposit_amount, deposit_pin)

# Check balance
check_balance_pin = input("Enter ATM PIN to check balance: ")
remaining_balance = account.check_balance(check_balance_pin)
if remaining_balance is not None:
    print(f"Remaining balance: {remaining_balance}")
