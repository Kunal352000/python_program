from numpy import*
x=array([
    [[50,51,52],[53,54,55]],
    [[60,61,62],[63,64,65]],
    [[70,71,72],[73,74,75]]
    ])
for i in x:
    for j in i:
        for k in j:
            print(k,end=" ")
        print()
    print()
