ch=input("Enter your charcter:").casefold()
if ch.isalpha():
    if ch=='a' or ch=='i' or ch=='e' or ch=='o' or ch=='u':
        print("Given charcter is vowel.")
    else:
        print("given charcter is consonent.")
else:
    print("given charcter is not alphabet")
    
