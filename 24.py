name=[]
num=int(input("Enter your number: "))
for i in range(num):
    name.append(input())
print("Befor sorting",name)
name.sort()
print("after sorting",name)
