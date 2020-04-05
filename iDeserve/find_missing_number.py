def find_missing(arr):
    start = 0
    end = len(arr)-1
    while end > start:
        mid = (start+end)//2
        if arr[mid] == mid+1:
            start = mid+1
        else:
            end = mid-1
    print(start+1)


arr = [1, 2, 3, 4, 6, 7, 8]
find_missing(arr)