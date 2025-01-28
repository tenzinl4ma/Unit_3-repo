import random

class BankCustomer:
    used_account_numbers = [] 
    bankname = "BANK OF PARADISE"
    def __init__(self, name, dob, email):
        self.name = name
        self.dob = dob
        self.email = email
        self.phone = None
        self.account_no = self.generate_account_no()
        self.balance = 0
    def generate_account_no(self, bankcode="031"):
        while True:  
            acc_number = "".join([str(random.randint(0, 9)) for _ in range(5)])
            account_no = f"{bankcode}-{acc_number}"
            if account_no not in BankCustomer.used_account_numbers:  
                BankCustomer.used_account_numbers.append(account_no)
                return account_no
    
    def deposit(self, amount: int):
        self.balance += amount
        return f"Deposited {amount} to {self.name}'s account. Current balance: {self.balance}"

    def withdraw(self, withdrew_amount: int):
        if withdrew_amount > self.balance:
            return f"Insufficient balance! Current balance: {self.balance}"
        self.balance -= withdrew_amount
        return f"Withdrawn {withdrew_amount}. Current balance: {self.balance}"

    def get_name(self):
        return self.name.title()

