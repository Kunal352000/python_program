str=input("Enter your String:")
words=str.split()
i=0
while i<len(words):
    if words[i][0] in 'aeiou' and words[i][-1] in 'aeiou':
        print(words[i])
    i+=1
