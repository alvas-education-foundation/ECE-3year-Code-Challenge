
for i in range(3) :
    name=input("Username")
    if name == "Micheal":
        pw=input("password")
        if pw == "e3$WT89x":
                print("Granted")
        elif pw!="e3$WT89x":
            print("Wrong password")

    else:
        print("Enter valid username")

    if i==2:
         print("Exceeded maximum try")

