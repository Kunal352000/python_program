A=list(int(i) for i in input().split(" "))
B=list(int(i) for i in input().split(" "))
cp=[(a,b) for a in A for b in B]
print(cp)
