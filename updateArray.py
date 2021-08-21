from array import*
arr1=[[1,2,3,4],[5,6,7,8]]
print("Before updating the array elements.")
print(arr1)

arr1[0]=[2,2,3,3]
arr1[1][2]=99
print("After updating the array elemets.")
for i in arr1:
    for x in i:
        print(x,end=" ")
    print()
