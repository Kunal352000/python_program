d={"kunal":345,"shivam":346,"kj":347,"sj":348}
k=input("Enter your key to be verified: ")
if k in d.keys():
    print("Key is present in the dictionary: ")
    print("values  :",d[k])
else:
    print("Key is not presnt in the list")
    
