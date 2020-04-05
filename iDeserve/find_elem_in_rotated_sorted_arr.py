def find_elem(arr, k):
    start, end = 0, len(arr)-1

    while start <= end:
        mid = (start+end)//2

        if arr[mid] == k:
            return mid

        # Check in sorted part of the array
        if arr[mid] < arr[end] and arr[mid] < k and arr[end] >= k :
            start = mid+1
            continue
        if arr[start] < arr[end] and arr[start] < k and arr[mid] >= k:
            end = mid-1
            continue

        # Check in rotated part
        if arr[mid] < arr[end] and arr[mid] < k:
            end = mid-1
        if arr[start] < arr[mid] and arr[mid] > k:
            start = mid +1

arr = [7, 8, 9, 2, 3, 4, 5, 6]
print(find_elem(arr, 4))