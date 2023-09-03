account_balance = 5000


while True:
    print(f'account balance: ${account_balance}')
    
    withdrawal_amount = int(input('Amount to withdraw: '))
    
    if withdrawal_amount > account_balance:
        print('Insuficient fund')
        break
    elif withdrawal_amount <= account_balance:
        account_balance -= withdrawal_amount
        print(f'${withdrawal_amount} has being removed; account balance: ${account_balance} left')
        
        again = input('Do you want to withdraw again? (y/n): ')
        
        if again == 'n':
            break
        elif again == 'y':
            continue
        else:
            print('Invalid input')
            break
    else:
        print('Insufficient funds. Please try again')
        continue    
    
        