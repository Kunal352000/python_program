#Break
for i in range(1,20,2):
    if(i%12==0):
        break
    print(i,end=" ")
else:
    print("im outside the loop:")
print(i)
