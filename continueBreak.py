while True:
    uname=input("Enter your username: ")
    if uname!="kunal":
        print("Invalid Username.")
        continue
    else:
        while True:
            pwd=input("Enter your password: ")
            if pwd=="kunal@123":
                break
            else:
                print("Invalid Password:")
                continue
        break
print("Congrates sucessfully login.")
