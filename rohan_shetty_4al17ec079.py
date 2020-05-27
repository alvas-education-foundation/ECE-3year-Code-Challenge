Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> username = "rohan"
password = "1234"
c = 0
while c < 3:
    a = input("enter the username")
    b = input("enter the password")
    if a == username and b == password:
        print("loged in successfully ")
        break
    else:
        c += 1
        if c ==3:
            print("you are blocked")
        else:
            print("try again")




