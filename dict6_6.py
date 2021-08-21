a={"kunal":111,"joshi":222,"shivam":333,"kj":444,123:555}
k=eval(input("Enter your key to be verfied: ")
if k in d.keys():
       print("key is present: ")
       print("value :",a[k]) 
else:
    print("key is not present in the dictionary")
