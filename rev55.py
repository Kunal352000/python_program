while True:
    uname=input("Enter your username: ")
    if uname!=' kunal':
        continue
    else:
        while True:
            pwd=input("Enter your password: ")
            if pwd=='kunal@123':
                break
            else:
                print("Invalid password. ")
                continue
        break
print("congrates sucessfully login.")
