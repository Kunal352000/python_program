ch=input("Enter your charcter:")
if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
    print("Given charcter is alphabet.")
elif ch>='0' and ch<='9':
    print("Given charcter is digit.")
else:
    print("Given charcter is special charcter.")
