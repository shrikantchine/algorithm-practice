def max_avg_subarr(arr, k):
    max_sum = sum(arr[:k])
    curr_sum = max_sum
    index = 0
    for i in range(k, len(arr)):
        curr_sum = curr_sum-arr[i-k]+arr[i]
        max_sum = max(curr_sum, max_sum)
        if max_sum == curr_sum:
            index = i

    print(arr[index-k+1:index+1])
    print(max_sum)

arr = [11, -8, 16, -7, 24, -2, 3]
k = 3
max_avg_subarr(arr, k)