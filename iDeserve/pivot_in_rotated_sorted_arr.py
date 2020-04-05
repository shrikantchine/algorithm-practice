def pivot(arr, start, end):
    if arr[start] < arr[end]:
        return 0
    while start <= end:
        mid = (start+end)//2
        if mid < len(arr)-2 and arr[mid] > arr[mid+1]:
            return mid+1
        if arr[start] > arr[mid]:
            end = mid-1
        else: 
            start=mid+1
    


arr = [7, 8, 9, 2, 3, 4, 5, 6]
print(pivot(arr, 0, len(arr)-1))