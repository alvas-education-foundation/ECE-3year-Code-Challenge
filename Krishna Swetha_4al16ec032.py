print('Enter username and password')
attempts=0
while attempts < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='e3$WT89x' and username=='Michael':
        print('Logged in successfully')
        break
    else:
        print('Invalid Username or password. Try again.')
        attempts += 1
if attempts==3 :
    print("Account Locked")