print('Enter username and password to continue')
cnt=0

while cnt<3:
    username=input('Enter username: ')
    password=input('Enter password: ')
    if password !='e3$WT89x' or username !='Micheal':
        print('Invalid username or Password')
        cnt+=1
    elif password=='e3$WT89x' and username=='Micheal':
        print('You have succesfully login')
    
        
    while cnt==3:
        print('Acnt locked')
        break
