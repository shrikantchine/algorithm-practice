def longest_consecutive_subsequence(arr):
    s = set(arr)
    max_len = 0
    for i in range(len(arr)):
        if (arr[i]-1) not in s:
            j = arr[i]
            while j in s:
                j += 1
            max_len = max(max_len, j-arr[i])
    return max_len

arr = [1, 9, 3, 10, 4, 20, 2]
print(longest_consecutive_subsequence(arr))