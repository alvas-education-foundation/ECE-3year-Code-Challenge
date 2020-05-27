"""Write python code to verify user_name = "Micheal" and password ="e3$WT89x". 
The total number of attempts are 03. For every wrong user_name and password 
Print - Invalid username or Password, upon three attempts fails print- Account locked
If inputs are correct Print - You have successfully login"""

#program to validate login details are correct or wrong
n=0
while n<3:
    username=input("Enter Username : ")
    password=input("Enter Password : ")
    if (username=="Micheal" and password=="e3$WT89x"):#successfull login condition
        print("successfully login")
        break
    else: #invalid user id and password block
        print(" Login failed check username or password")
        n+=1
        if n==3:#maximum no.of attempt block
            print('Account locked')
            break
