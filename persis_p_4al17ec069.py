# -*- coding: utf-8 -*-
"""Persis P 4AL17EC069.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vVXUNwh_ruBZr_ZwGDvcbG3fBAbab38G
"""

count=0
while count<3:
    user_name=input("Enter the username: ")
    password =input("Enter the password :")
    if user_name =="Micheal" and password =="e3$WT89x":
            print("You have successfully logged in")
    else:
            count+=1
            print("Invalid username and password")
            if count==3:
             print("Account Locked")