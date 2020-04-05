def peak_element(arr):
    start, end = 0, len(arr)-1
    mid = (end+start)//2
    if (mid == end or arr[mid] > arr[mid+1]) and (mid == 0 or arr[mid] > arr[mid-1]):
        return arr[mid]
    if (mid > 0 and arr[mid] < arr[mid-1]):
        return peak_element(arr[:mid])
    if (mid < end and arr[mid] < arr[mid+1]):
        return peak_element((arr[mid+1:]))


arr = [40, 10, 20, 5, 45, 50, 65, 90, 35, 25]
print(peak_element(arr))

arr = [40, 20, 10, 5]
print(peak_element(arr))

arr = [4, 10, 20, 50]
print(peak_element(arr))