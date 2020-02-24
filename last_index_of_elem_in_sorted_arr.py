def last_index(arr, k):
    start, end = 0, len(arr)-1
    while start <= end:
        mid = (end+start)//2
        if arr[mid] == k and (mid == end or arr[mid+1] > k):
            return mid
        elif k < arr[mid]:
            end = mid-1
        else:
            start = mid +1
    return -1



arr = [0, 1, 2, 2, 4, 5, 5, 5, 8]
k = 5
print(last_index(arr, k))