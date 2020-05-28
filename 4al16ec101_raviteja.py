Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def login (user_name):
print('enter user name')
def login (password):
print('enter correct password');
count=0
while count<3:
user_name=input('enter user name:')
if user_name=='Micheal':
password=input('enter password;')
if password=='e3$WT89x':
count=5
elif password!=1:
print("incorrect")
count+=1
else:
print("you tried too many times,locked")
count>=3
