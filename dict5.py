x={'m':39,'sc':78,'so':71,'tel':78}
print(len(x))
print(min(x))
print(min(x.items()))
print(min(x.values()))
print(max(x))
print(max(x.items()))
print(max(x.values()))
print(sorted(x))
print((reversed(x)))
for i in reversed(x):
    print(i)
print(sorted(x.items()))
print(sorted(x.items(),reverse=True))
print(sorted(x.values()))
print(reversed(x.items()))
for i in reversed(x.items()):
    print(i)
print(reversed(x.values()))
for i in reversed(x.values()):
    print(i)
print(list(reversed(x.keys())))
for i in reversed(x.keys()):
    print(i)
