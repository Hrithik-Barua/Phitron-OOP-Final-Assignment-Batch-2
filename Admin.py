
from Bank import Bank

class Admin(Bank):
    

    def __init__(self,name,phone_number,email,id) -> None:
        self.name = name
        self.account_number = 0
        self.phone_number = phone_number
        self.email = email
        self.id_no = id
    
    def create_account(self,account_number):
        if account_number in Bank.accounts:
            print(f'this account number have already been exists!,please try another number')
        else:
            self.account_number = account_number
            Bank.accounts[self.account_number] = (self.account_number,self.name,self.email,self.id_no)

            print(f'account created successfully!,with name {self.name} and account number: {self.account_number}')

    def check_total_balance(self):
        total_balance = self.total_balance
        return total_balance

    def check_total_loan(self):
        return self.total_amount_loan
    
    def all_transaction(self):
        return self.transactions_history
    
    def toggle_loan_feature(self, value):
        Bank.is_loan_enable = value
