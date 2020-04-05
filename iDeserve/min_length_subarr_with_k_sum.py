def min_subarr(arr, k):
    min_arr = arr
    curr_arr = []
    curr_sum = 0
    for x in arr:
        curr_sum += x
        curr_arr.append(x)
        while curr_sum >= k:
            if curr_sum == k:
                min_arr = min_arr.copy() if len(min_arr) < len(curr_arr) else curr_arr.copy()
            y = curr_arr.pop(0)
            curr_sum -= y
    print(min_arr)



arr = [2, 3, 1, 1, -1, 6, 4, 3, 8]
k = 7
min_subarr(arr, k)