ch=input("Enter the charcter: ")
if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
    if ch=='a' or ch=='i' or ch=='e' or ch=='o' or ch=='u' or\
       ch=='A' or ch=='I' or ch=='E' or ch=='O' or ch=='U':
        print("given charcter is vowel")
    else:
        print("given charcter is consonent.")
else:
    print("given charcter is not alphabet.")
