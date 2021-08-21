str=input("Enter your string: ").casefold()
print({i:len(i) for i in str.split()})
