n1=int(input())
set1=set(int(i) for i in input().split(" "))

n2=int(input())
set2=set(int(i) for i in input().split(" "))

inter=set1.intersection(set2)
print(inter)
print(len(inter))
