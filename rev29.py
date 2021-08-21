s1=input("Enter yoyr s2 String.").casefold()
s2=input("Enter your s1 String.").casefold()
if len(s1)==len(s2):
    if sorted(s1)==sorted(s2):
        print("Given String are anagram String")
    else:
        print("Given String are not a anagram String.")
else:
    print("not a anagram string")
