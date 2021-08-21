ch=input("Enter your charcter:").casefold()
if ch.isalpha():
    print("Alphabet.")
elif ch.isdigit():
    print("Digit.")
else:
    print("Specail charcter.")
