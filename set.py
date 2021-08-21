def average(array):
    array=set(array)
    return (sum(array)/len(array))


    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
