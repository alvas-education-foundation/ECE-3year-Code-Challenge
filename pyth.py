#def fun(login):
count=0
while count < 4:
     input1= input ("enter your name :")
     input2= input("enter your password:")
     print (input1,input2)

     if input1 == "Micheal" and input2 == "e3$WT89x":
         print ("login is successful")
     else:
         print("invalid")

         count +=1
        
     if count >3:
             print("your account is blocked")
         
           
