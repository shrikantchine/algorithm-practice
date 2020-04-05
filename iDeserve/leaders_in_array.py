def find_leaders(arr):
    result = [arr[-1]]
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > result[-1]:
            result.append(arr[i])
    print(result)

arr = [98, 23, 54, 12, 20, 7, 27]
find_leaders(arr)