class BankAccount:
    def __init__(self, account_number, pin, balance=0, account_name=""):
        self.account_number = account_number
        self.account_name = account_name
        self._pin = pin
        self._balance = balance

    # Validate PIN
    def validate_pin(self, entered_pin):
        return self._pin == entered_pin

    # Check balance
    def check_balance(self):
        print(f"Account Holder: {self.account_name}")
        print(f"Current Balance: {self._balance}")

    # Deposit Money
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposit Successful. New Balance: {self._balance}")
        else:
            print("Invalid deposit amount.")

    # Withdraw Money
    def withdraw_money(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawal Successful. New Balance: {self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    # Change PIN
    def change_pin(self, old_pin, new_pin):
        if self.validate_pin(old_pin) and len(new_pin) == 4 and new_pin.isdigit():
            self._pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Invalid old PIN or new PIN.")

    # Change Account Name
    def change_account_name(self, new_name):
        if new_name.strip():
            self.account_name = new_name
            print(f"Account name changed to: {self.account_name}")
        else:
            print("Invalid name.")


class ATM:
    def __init__(self):
        self.accounts = {}

    # Create account
    def create_account(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")
        name = input("Enter your account holder name: ")
        if len(pin) == 4 and pin.isdigit():
            self.accounts[account_number] = BankAccount(account_number, pin, account_name=name)
            print("Account created successfully.")
        else:
            print("Invalid PIN. Must be 4 digits.")

    # Authenticate account
    def authenticate_account(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")
        if account_number in self.accounts:
            if self.accounts[account_number].validate_pin(pin):
                print("Authentication successful.")
                return self.accounts[account_number]
            else:
                print("Invalid PIN.")
        else:
            print("Invalid account number.")
        return None

    # Account menu
    def account_menu(self, account):
        while True:
            print("\n--- ATM Menu ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. Change Account Name")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                account.check_balance()
            elif choice == "2":
                amount = input("Enter amount to deposit: ")
                if amount.isdigit():
                    account.deposit(int(amount))
                else:
                    print("Invalid amount.")
            elif choice == "3":
                amount = input("Enter amount to withdraw: ")
                if amount.isdigit():
                    account.withdraw_money(int(amount))
                else:
                    print("Invalid amount.")
            elif choice == "4":
                old_pin = input("Enter your old PIN: ")
                new_pin = input("Enter your new 4-digit PIN: ")
                account.change_pin(old_pin, new_pin)
            elif choice == "5":
                new_name = input("Enter your new account name: ")
                account.change_account_name(new_name)
            elif choice == "6":
                print("Logging out...")
                break
            else:
                print("Invalid choice.")

    # Main menu
    def main_menu(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose an option (1-3): ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                account = self.authenticate_account()
                if account:
                    self.account_menu(account)
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    atm = ATM()
    atm.main_menu()
