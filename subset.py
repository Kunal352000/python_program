t=int(input())
for i in range(t):
    A=int(input())
    set1=set(int(i) for i in input().split(" "))

    B=int(input())
    set2=set(int(i) for i in input().split(" "))

print(set1.issubset(set2))
    
