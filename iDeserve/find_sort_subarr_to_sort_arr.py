def find_subarr(arr):
    # Find out of order index from left - m
    m = 0
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            m = i-1
            break
    # find out of order index from right - n
    n=len(arr)-1
    for i in range(len(arr)-2, -1, -1):
        if arr[i+1] < arr[i]:
            n = i+1
            break

    print(f"{m} - {n}")
    print(arr[m:n+1])
    # find min and max element in arr[m-n]
    min_elem = min(arr[m:n+1])
    max_elem = max(arr[m:n+1])
    print(f"{min_elem} - {max_elem}")
    # find element less than min in arr[0-m]
    start_index=m
    for i in range(m, -1, -1):
        if arr[i] < min_elem:
            start_index = i+1
            break
    # find element greater that max in arr[n:]
    end_index = n
    for i in range(n, len(arr), 1):
        if arr[i] < max_elem:
            end_index = i
    print(f"{start_index} - {end_index}")


# arr = [1, 4, 7, 5, 10, 18, 17, 26, 30, 45, 50, 62]
arr = [1, 4, 7, 3, 10, 48, 17, 26, 30, 45, 50, 62]
find_subarr(arr)