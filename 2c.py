#captcha program
import random
uid=input("Enter userid=>")
pwd=input("Enter password=>")
if(uid=="FirstBit" and pwd=="Python"):
    captcha=random.randint(1000,10000)
    print("Enter captcha",captcha)
    data=int(input("Enter captcha:"))
    if(data==captcha):
        print("Login Succesful")
    else:
        print("Invalid captcha")
else:
    print("Login failed")
