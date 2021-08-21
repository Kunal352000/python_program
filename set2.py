n=int(input())
set1=set(int(i) for i in input(" ").split(" "))

n1=int(input())
set2=set(int(i) for i in input(" ").split(" "))

U=set1.union(set2)
Intr=set1.intersection(set2)

sym=U-Intr
List1=[i for i in sym]
List1.sort()
for i in List1:
    print(i)
