import random
uname=input("Enter user name=>")
password=input("Enter password=>")

if(uname=="FirstBit" and password=="python"):
    captcha=random.randint(1000,10000)
    print("Enter capcha=>",captcha)
    data=int(input("Enter captcha=>"))
    if(data==captcha):
        print("Login Succesful")
    else:
        print("Invalid captcha")

else:
    print("Login failed")
