x=input("Enter the string.")
words=x.split()
i=0
while i<len(words):
    if words[i][0] in 'aeiou':
        print(words[i])
    i+=1
