
class Bank:
    accounts = {}
    admin_accounts = {}
    __total_balance = 0 
    total_loan = []
    total_amount_loan = 0
    transactions_history = {}
    is_loan_enable = True

    @property
    def total_balance(self):
        return self.__total_balance
    
    @total_balance.setter
    def total_balance(self,amount):
        self.__total_balance = amount


    def add_transaction(account_number,transactions):
        if account_number in Bank.transactions_history:
            Bank.transactions_history[account_number].append(transactions)
        else:
            Bank.transactions_history[account_number] = [transactions]

    