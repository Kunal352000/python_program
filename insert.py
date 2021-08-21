from array import*
array1=[[12,23,43,22,11],[21,34,45,66,77]]
print("Before inserting element.")
print(array1)
array1.insert(0,[5,6,7,8,9])
print("After inseting element.")

for i in array1:
    for x in i:
        print(x,end=" ")
    print()
