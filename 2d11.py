from numpy import*
x=array([
    [50,51,52,53,54,55],
    [60,61,62,64,78],
    [70,71,72],
    [80,81,82,00,98]
    ])
i=0
while i<4:
    j=0
    while j<len(x[i]):
        print(x[i][j],end=" ")
        j+=1
    print()
    i+=1
