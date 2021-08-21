x=input("Enter the string: ").casefold()
i=0
while i<len(x):
    if x[i] in 'aeiou':
        print(x[i])
    i+=1
