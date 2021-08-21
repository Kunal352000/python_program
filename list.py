list=[ ]
n=int(input(""))
for i in range(n):
    x=input("").split(" ")
    cmd=x[0]
    if cmd=="append":
        list.append(int(x[1]))
        
    if cmd=="insert":
        list.insert(int(x[1]),int(x[2]))

    if cmd=="remove":
        list.remove(int(x[1]))
        
    if cmd=="sort":
        list.sort()
        
    if cmd=="pop":
        list.pop()
        
    if cmd=="reverse":
        list.reverse()

    if cmd=="print":
        print(list)
       

    

