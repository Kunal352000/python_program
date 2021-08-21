#login
for i in range(3):
    uid=input("Enter userid:")
    pwd=input("Enter password:")
    if(uid=="FirstBit"and pwd=="Python"):
        break
        print("Login Succesful")
    else:
        print("Try more")
else:
    print("Login failed")
     
