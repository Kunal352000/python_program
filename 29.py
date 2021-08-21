name=[]
marks=[]
for i in range(5):
    n=input("Enter your name: ").upper()
    name.append(n)
print("Entered names are =",name)
name.sort()
print("Sorted names are =",name)
