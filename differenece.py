n=int(input())
set1=set(int(i) for i in input().split(" "))

n1=int(input())
set2=set(int(i) for i in input().split(" "))

diff=set1.difference(set2)
print(diff)
print(len(diff))
