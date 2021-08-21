n1=int(input())
set1=set(int(i) for i in input().split(" "))

n2=int(input())
set2=set(int(i) for i in input().split(" "))

Sym_diff=set1.symmetric_difference(set2)
print(Sym_diff)
print(len(Sym_diff))
