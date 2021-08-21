n=int(input())
set1=set(int(i) for i in input().split(" "))

n1=int(input())
set2=set(int(i) for i in input().split(" "))

U=set1.union(set2)
print(U)
print(len(U))
