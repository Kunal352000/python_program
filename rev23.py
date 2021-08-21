ch=input("Enter the charcter:")
if ch.isalpha():
    if ch.islower():
        print("lower case.")
    else:
        print("upper case.")
else:
    print("given character is not alphabet.")
