st=input("Enter your String:").casefold()
if st==st[::-1]:
    print("Given String is palindrome")
else:
    print("Given String is not palindrome")
