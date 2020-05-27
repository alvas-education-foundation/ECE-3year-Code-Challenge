def new(user_name, password):
    if user_name == "Micheal" and password == "e3$WT89x":
        return "login sucessful"
    attempt = 0
    while attempt <=3:
        if attempt == 2:
            return "you account has been locked"
        else:
            print ("Invalid username or password")
            x= input ("Enter username: ")
            y = input ("Enter Password: ")
            if x== "Micheal" and y == "e3$WT89x":
                return "login sucessful"
            attempt = attempt+1

x= input("Enter username: ")
y = input("Enter Password: ")
print(new(x,y))