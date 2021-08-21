st=input("Enter the string:-")
words=st.split()
i=0
while i<len(words):
    if words[i] in words[i].startswith('a'):
        print(words[i])
    i+=1
