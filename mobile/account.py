
account_balance = 5000

def withdraw_money():
    global account_balance
    while True:
        print(f'account balance: ${account_balance}')
        withdrawal_amount = int(input('Amount to withdraw: '))
        if account_balance == 0:
            print("You can't withdraw")
            break       
        elif withdrawal_amount <= account_balance:
            account_balance -= withdrawal_amount
            print(f'${withdrawal_amount} has being removed; account balance: ${account_balance} left')
            continue_withdrawal()
        else:
            print('Insufficient funds. Please try again')
            continue    

def continue_withdrawal():
        continue_ = input('Do you want to withdraw again? (y/n): ')
           
        if continue_ == 'n':
            return exit('Thank you and good bye')
        elif continue_ == 'y':
            return withdraw_money()
        else:
            print('Invalid input')
            continue_withdrawal()      

withdraw_money()