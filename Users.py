from Bank import Bank

class User(Bank):

    __total_balance =0

    def __init__(self,name,phone_number,account_number,email) -> None:
        
        self.name = name
        self.account_number = account_number
        self.phone_number = phone_number
        self.email = email
        self.__balance  = 0

    # User can create an account
    def create_account(self):
        if self.account_number in Bank.accounts:
            print('this account number have already been exists,please try another number')
        else:
            Bank.accounts[self.account_number] = (self.account_number,self.name,self.phone_number,self.email)

            print(f'congratulations!,you have created an account successfully with account name : {self.name} and account number : {self.account_number}')

    # User can deposit    
    def deposit(self,amount):
        # print('you have to deposit minimum 1000 taka only')
        if amount >= 1000:
            self.__balance += amount
            User.__total_balance +=amount
            Bank.total_balance = User.__total_balance

            transaction = f'Deposit: {amount} to account name : {self.name} and account number :{self.account_number}'
            Bank.add_transaction(self.account_number,transaction)

            print(f'Deposit successfully, with {amount} taka. Now ,your current balance is : {self.__balance}')

    # User can withdraw    
    def withdraw(self,amount):
        if User.__total_balance <= 0:
            print('Bank is Bankrupt!')
        elif amount >= self.__balance:
            print('sorry!,you have insufficient balance.')
        else:
            self.__balance -= amount
            User.__total_balance -= amount
            Bank.total_balance = User.__total_balance

            transaction = f'withdraw: {amount} taka from the account name :{self.name} and account number : {self.account_number}'
            Bank.add_transaction(self.account_number,transaction)

            print(f'Withdraw successfully done with amount {amount} taka. Now your current balance is : {self.__balance}')

    # User can transfer money
    def transfer_money(self,recipient,amount):
        if recipient != self and amount>0 and amount <= self.__balance:
            recipient.__balance += amount
            self.__balance -= amount

            transaction_1 = f'transfer: {amount} taka  to account  number: {recipient.account_number} with account name: {recipient.name}'

            transaction_2 = f'Receive: {amount} taka from account number:  {self.account_number} with account name: {self.name}'

            Bank.add_transaction(self.account_number,transaction_1)
            Bank.add_transaction(recipient.account_number,transaction_2)

            print(f'transfer successfully! ,with amount {amount} taka from {self.name} with account number:  {self.account_number} to {recipient.name} with account number: {recipient.account_number}.Now your current balance is : {self.__balance}')

    # User can take loan
    def take_loan(self,amount):
        if Bank.is_loan_enable:
            max_loan = self.__balance*2
            if amount <= max_loan:
                self.__balance += amount
                User.__total_balance -= amount
                Bank.total_balance = User.__total_balance
                Bank.total_amount_loan += amount
                Bank.total_loan.append((self.account_number,amount))

                transaction = f'Loan: {amount} taka for account : {self.account_number} with account name: {self.name}'
                Bank.add_transaction(self.account_number,transaction)

                print(f'Loan taken successfully !, with amount: {amount} for account: {self.account_number} with name: {self.name}.Now your current balance is : {self.__balance}')
        else:
            print(f'sorry {self.name} !,Bank has stopped to give loan. Please Wait for few days. ')

    # User can check balance
    def check_balance(self):
        print(f' Hey {self.name}!, Your current balance is : {self.__balance}') 
        return ''

    # User can get transaction history
    def get_transaction_history(self):
        if self.account_number in Bank.transactions_history:
            return Bank.transactions_history[self.account_number]