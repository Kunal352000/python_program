dic={'kunal':12,"joshi":13,"shivam":14,"ss":15}
k=input("Enter your key to be verified: ")
for i in dic.keys():
    if i==k:
        print("key is presnet")
        print("value:",dic[k])
else:
    print("Key is not present.")
