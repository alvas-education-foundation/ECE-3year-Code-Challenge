count=0
while count<3:
    user=input("Enter the username\n")
    pw=input("Enter the password\n")
    if user=="Micheal" and pw=="e3$WT89x":
        print("Permission granted")
        break
    else:
        print("Wrong username or password try again")
        count+=1
    if count==3:
        print("Account is locked")