ch=input("Enter your charcter:").casefold()
if ch.isalpha():
    if ch in 'aeiou':
        print("given charcter is vowel.")
    else:
        print("given charcter is consonent.")
else:
    print("given charcter is not alphabet.")
