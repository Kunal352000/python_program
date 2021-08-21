from array import*
arr1=[1,2,3,4],[5,6,7,8]
print("before delting the elements.")
print(arr1)

del(arr1[0][1])
#del(arr1[1])

print("After delting the elements.")
for i in arr1:
    for x in i:
        print(x,end=" ")
    print()
