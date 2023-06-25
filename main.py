

from Users import User
from Admin import Admin

def main():
    akib = User('akib khan',88018149,112301,'akib@gmail.com')
    akib.create_account()
    akib.deposit(1000)
    akib.deposit(1200)
    akib.withdraw(500)

    rahim = User('rahim rahman',88016341,112401,'rahim@gamil.com')
    rahim.create_account()
    rahim.deposit(1500)
    rahim.deposit(10000)
    rahim.withdraw(1000)

    rahim.transfer_money(akib,2000)

    
    rahim.check_balance()
    akib.check_balance()

   
    rahim.take_loan(1000)
      

    akib_transaction_history = akib.get_transaction_history()
    print('...........Your(akib) transaction history is :- .........')
    for transaction in akib_transaction_history:
        print(transaction)

   

    rahim_transaction_history = rahim.get_transaction_history()
    print('......Your(rahim)) transaction history is :-......... ')
    for transaction in rahim_transaction_history:
        print(transaction)
    
    zaman = Admin('Md Zaman',88018661,'zaman.admin@gmail.com',201336)
    zaman.create_account(113301)

    total_balance_of_bank = zaman.check_total_balance()
    print(f'total balance of bank is: ',total_balance_of_bank ,' taka')

    print(f'The bank given total : ',zaman.check_total_loan(),' taka loan')

    all_transaction_of_bank = zaman.all_transaction()
    print(f'-------------all transaction of bank: -----------')
    for account_number,transactions in all_transaction_of_bank.items():
        print('Account number : ',account_number)
        for transaction in transactions:
            print(transaction)


    zaman.toggle_loan_feature(False)
    rahim.take_loan(1200)
    akib.take_loan(500)


if __name__ == '__main__':
    main()