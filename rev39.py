x=input("Enter the string: ")
l_c=0
u_c=0
i=0
while i<len(x):
    if x[i].islower():
        l_c+=1
    elif x[i].isupper():
        u_c+=1
    i+=1
print("Lower case no =",l_c)
print("Upper case no =",u_c)
