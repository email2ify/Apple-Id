attempts = 6
secret_number = 10

while attempts > 0:

    user_number = int(input('What is your pin number? '))
    
    if user_number == secret_number:
        print('You are logged in')
        break
        
    else:
        attempts -=1
        print(f'failed you have {attempts} attempts left')
        