from numpy import*
x=array([
    [50,51,52,53,54,55],
    [60,61,62,64,78],
    [70,71,72],
    [80,81,82,00,98]
    ])
for i in x:
    for j in i:
        print(j,end=" ")
    print()
