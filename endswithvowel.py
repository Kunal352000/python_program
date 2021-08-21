str=input("Enter your string:")
words=str.split()
i=0
while i<len(words):
    if words[i][-1] in 'aeiou':
        print(words[i])
    i+=1
