
#Write python code to verify user_name = "Micheal" and password ="e3$WT89x". The total number of attempts are 03. For every wrong user_name and password Print - Invalid username or Password, upon three attempts fails print- Account locked. If inputs are correct Print - You have successfully login



def para(user_name, password):
    if user_name == "Micheal" and password == "e3$WT89x":
        return "login sucessful"
    attempt = 0
    while attempt <=3:
        if attempt == 2:
            return "you account has been locked"
        else:
            print ("Invalid username or password")
            a = input ("Enter username: ")
            b = input ("Enter Password: ")
            if a == "Micheal" and b == "e3$WT89x":
                return "login sucessful"
            attempt = attempt+1

a = input("Enter username: ")
b = input("Enter Password: ")
print(para(a,b))
