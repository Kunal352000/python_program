ch=input("Enter the character: ").casefold()
if ch.isalpha():
    if ch in ['a','e','i','o','u']:
        print("Given charcter is vowel.")
    else:
        print("Given charcter is consonent.")
else:
    print("Given character is not alphabet.")
